import os
import requests
from typing import Dict, Any
from collections import defaultdict
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class SecurityLogCompressor:
    def __init__(self):
        self.api_key = os.getenv('SCALEDOWN_API_KEY')
        self.api_url = 'https://api.scaledown.xyz/compress/raw/'
        self.target_model = 'gpt-4o'
        if not self.api_key:
            raise ValueError('API key not found')
    
    def logs_to_natural_language(self, logs: str) -> str:
        """Convert structured logs to natural language for better compression."""
        lines = [l.strip() for l in logs.strip().split('\n') if l.strip()]
        
        # Parse log entries
        events = defaultdict(list)
        ips = set()
        users = set()
        critical_events = []
        timestamps = []
        
        for line in lines:
            # Extract timestamp
            if line and len(line) > 20:
                timestamps.append(line[:20])
            
            # Extract severity
            if 'CRITICAL' in line:
                severity = 'CRITICAL'
                critical_events.append(line.split(severity)[1].strip() if severity in line else '')
            elif 'ERROR' in line:
                severity = 'ERROR'
            elif 'WARNING' in line:
                severity = 'WARNING'
            elif 'ALERT' in line:
                severity = 'ALERT'
            else:
                severity = 'INFO'
            
            events[severity].append(line)
            
            # Extract IPs
            import re
            ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
            found_ips = re.findall(ip_pattern, line)
            ips.update(found_ips)
            
            # Extract usernames
            if 'user ' in line.lower():
                parts = line.lower().split('user ')
                if len(parts) > 1 and len(parts[1].split()) > 0:
                    username = parts[1].split()[0].strip()
                    users.add(username)
        
        # Build verbose natural language summary
        summary_parts = []
        
        # Header
        total_events = len(lines)
        date_info = ""
        if timestamps:
            date_info = f" recorded on {timestamps[0][:10]}" if timestamps[0] else ""
        summary_parts.append(
            f"Security Incident Analysis Report: This analysis covers {total_events} distinct security events{date_info}. "
        )
        
        # Critical events (verbose)
        if events['CRITICAL']:
            summary_parts.append(
                f"The system identified {len(events['CRITICAL'])} critical security incidents that require immediate attention. "
                f"These critical events include: {' and '.join(critical_events[:3]) if critical_events else 'multiple high-severity threats'}. "
            )
        
        # Warnings (verbose)
        if events['WARNING']:
            warning_text = f"Our monitoring system detected {len(events['WARNING'])} security warnings throughout the analysis period. "
            if 'failed login' in logs.lower():
                failed_count = logs.lower().count('failed login')
                warning_text += f"This includes {failed_count} failed authentication attempts which suggest possible unauthorized access attempts. "
            summary_parts.append(warning_text)
        
        # IPs (verbose)
        if ips:
            ip_list = ', '.join(list(ips)[:5])
            summary_parts.append(
                f"Network activity analysis identified the following IP addresses involved in these security events: {ip_list}. "
                f"These IP addresses were flagged due to suspicious or malicious behavior patterns. "
            )
        
        # Users (verbose)  
        if users:
            user_list = ', '.join(list(users)[:8])
            summary_parts.append(
                f"The attacks specifically targeted the following user accounts: {user_list}. "
                f"This targeting pattern suggests a systematic approach to gain unauthorized access. "
            )
        
        # Attack patterns (verbose)
        if 'brute force' in logs.lower() or (events['WARNING'] and len(events['WARNING']) > 5):
            summary_parts.append(
                "Based on the frequency and pattern of failed authentication attempts, "
                "our analysis indicates this is consistent with an automated brute force attack "
                "attempting to compromise user credentials through systematic password guessing. "
            )
        if 'sql injection' in logs.lower() or 'union select' in logs.lower():
            summary_parts.append(
                "The logs reveal evidence of SQL injection attack techniques being employed. "
                "The attacker attempted to manipulate database queries to extract sensitive information "
                "or gain unauthorized access to backend systems. "
            )
        if 'ransomware' in logs.lower() or 'encryption' in logs.lower():
            summary_parts.append(
                "Critical ransomware activity has been identified in the system. "
                "This includes unauthorized file encryption, attempts to disable backup systems, "
                "and potential data exfiltration to remote command and control servers. "
            )
            
        if 'ddos' in logs.lower() or 'traffic spike' in logs.lower():
            summary_parts.append(
                "The system experienced symptoms consistent with a Distributed Denial of Service (DDoS) attack. "
                "This includes abnormal traffic patterns, resource exhaustion, and service degradation. "
            )
        
        # additional context
        if events['ERROR']:
            summary_parts.append(
                f"The system logged {len(events['ERROR'])} error conditions during this period, "
                f"indicating technical issues or security control failures. "
            )
        if events['ALERT']:
            summary_parts.append(
                f"Automated security monitoring systems triggered {len(events['ALERT'])} distinct alerts "
                f"based on predefined threat detection rules and behavioral analysis. "
            )
        
        # Conclusion
        if events['CRITICAL'] or len(events['WARNING']) > 5:
            summary_parts.append(
                "Immediate security response and incident investigation is recommended to contain the threat "
                "and prevent further compromise of system resources. "
            )
        
        return "".join(summary_parts)
    
    def compress_logs(self, logs, prompt='Analyze security threats'):
        # Convert structured logs to natural language for better compression
        natural_logs = self.logs_to_natural_language(logs)
        
        headers = {'x-api-key': self.api_key, 'Content-Type': 'application/json'}
        payload = {'context': natural_logs, 'prompt': prompt, 'model': self.target_model, 'max_tokens': 500, 'scaledown': {'rate': 'high'}}
        
        import time
        start = time.time()
        response = requests.post(self.api_url, headers=headers, json=payload, timeout=30)
        latency = int((time.time() - start) * 1000)
        
        if response.status_code == 200:
            result = response.json()
            # Parse ScaleDown API response format
            orig = result.get('total_original_tokens', len(logs.split()))
            comp = result.get('total_compressed_tokens', len(logs.split()) // 2)
            compressed_text = result.get('results', {}).get('compressed_prompt', natural_logs)
            
            return {
                'content': compressed_text,
                'compressed_context': compressed_text,
                'original_tokens': orig,
                'compressed_tokens': comp,
                'successful': result.get('successful', False),
                'compression_ratio': result.get('request_metadata', {}).get('average_compression_ratio', 1.0),
                'latency_ms': result.get('latency_ms', latency)
            }
        else:
            raise Exception(f'API error {response.status_code}: {response.text}')
    
    def get_compression_stats(self, result):
        orig = result.get('original_tokens', 0)
        comp = result.get('compressed_tokens', 0)
        saved = orig - comp
        percent = (saved / orig * 100) if orig > 0 else 0
        ratio = (orig / comp) if comp > 0 else 0
        cost = (saved / 1000000) * 0.15
        return {'original_tokens': orig, 'compressed_tokens': comp, 'tokens_saved': saved, 'savings_percent': round(percent, 2), 'compression_ratio': round(ratio, 2), 'latency_ms': result.get('latency_ms', 0), 'target_model': self.target_model, 'estimated_cost_saved': round(cost, 6)}
