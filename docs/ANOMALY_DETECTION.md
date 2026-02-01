# Anomaly Detection Documentation

**Module:** `src/detector.py`  
**Last Updated:** February 1, 2026  
**Status:** ✅ Implemented

---

## 📋 Overview

The `SecurityLogDetector` class provides AI-powered and pattern-based anomaly detection for security logs. It identifies threats, calculates severity levels, and provides actionable recommendations.

### Detection Methods
1. **Pattern-Based Detection** - Fast, regex-based threat identification
2. **AI-Powered Detection** - Deep analysis using GPT models (optional)

### Key Features
- 8 built-in threat patterns
- Confidence scoring
- Severity classification
- Automatic indicator extraction (IPs, usernames)
- Deduplication and prioritization
- Overall threat level calculation

---

## 🎯 Threat Types Detected

| Anomaly Type | Severity | Description |
|--------------|----------|-------------|
| **Brute Force Attack** | HIGH | Multiple failed login attempts |
| **Unauthorized Access** | MEDIUM | Access denied/forbidden attempts |
| **Suspicious Traffic** | CRITICAL | Unusual network connections |
| **Data Exfiltration** | CRITICAL | Large/unusual data transfers |
| **Privilege Escalation** | HIGH | Sudo/root access attempts |
| **SQL Injection** | CRITICAL | SQL injection attack attempts |
| **Malware Activity** | CRITICAL | Virus/ransomware/trojan detected |
| **Failed Authentication** | MEDIUM | Account lockouts |

---

## 🔧 Class: SecurityLogDetector

### Initialization

```python
from src.detector import SecurityLogDetector

# Pattern-based only (fast, no API calls)
detector = SecurityLogDetector(ai_enabled=False)

# With AI enhancement (requires OpenAI API key)
detector = SecurityLogDetector(
    ai_enabled=True,
    openai_api_key="your-openai-key"
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ai_enabled` | bool | False | Enable AI-powered deep analysis |
| `openai_api_key` | str | None | OpenAI API key (from env if not provided) |

---

## 📖 Methods

### detect_anomalies()

Main detection method - analyzes logs and returns anomalies.

```python
anomalies = detector.detect_anomalies(
    logs=security_logs,
    compressed_context=compressed_logs  # Optional, for AI analysis
)
```

**Parameters:**
- `logs` (str): Raw security log text
- `compressed_context` (str, optional): Compressed logs from ScaleDown for AI analysis

**Returns:**  
`List[Anomaly]` - Detected anomalies sorted by severity

### calculate_threat_level()

Calculate overall threat level from detected anomalies.

```python
overall_threat = detector.calculate_threat_level(anomalies)
```

**Returns:**  
`ThreatLevel` enum: CRITICAL, HIGH, MEDIUM, LOW, or INFO

---

## 📊 Data Structures

### Anomaly (Dataclass)

```python
@dataclass
class Anomaly:
    type: AnomalyType              # Type of threat
    severity: ThreatLevel          # Severity level
    description: str               # Human-readable description
    recommendation: str            # Security recommendation
    confidence: float              # Confidence score (0.0-1.0)
    affected_resources: List[str]  # IPs, usernames, etc.
    timestamp: Optional[str]       # When detected
    indicators: Optional[List[str]] # Pattern matches
```

### ThreatLevel (Enum)

```python
class ThreatLevel(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"
```

### AnomalyType (Enum)

```python
class AnomalyType(Enum):
    BRUTE_FORCE = "Brute Force Attack"
    UNAUTHORIZED_ACCESS = "Unauthorized Access Attempt"
    SUSPICIOUS_TRAFFIC = "Suspicious Network Traffic"
    DATA_EXFILTRATION = "Potential Data Exfiltration"
    PRIVILEGE_ESCALATION = "Privilege Escalation"
    MALWARE_ACTIVITY = "Malware Activity"
    SQL_INJECTION = "SQL Injection Attempt"
    XSS_ATTACK = "Cross-Site Scripting"
    DOS_ATTACK = "Denial of Service"
    UNUSUAL_PATTERN = "Unusual Activity Pattern"
    FAILED_AUTH = "Failed Authentication"
    ACCOUNT_COMPROMISE = "Potential Account Compromise"
```

---

## 💡 Usage Examples

### Example 1: Basic Pattern Detection

```python
from src.detector import SecurityLogDetector

# Sample logs
logs = """
2026-02-01 10:24:12 WARN Failed login attempt for user root from 203.0.113.45
2026-02-01 10:24:15 WARN Failed login attempt for user root from 203.0.113.45
2026-02-01 10:24:18 WARN Failed login attempt for user root from 203.0.113.45
"""

# Detect
detector = SecurityLogDetector()
anomalies = detector.detect_anomalies(logs)

# Display
for anomaly in anomalies:
    print(f"{anomaly.type.value} - {anomaly.severity.value}")
    print(f"  {anomaly.description}")
    print(f"  Action: {anomaly.recommendation}")
```

**Output:**
```
Brute Force Attack - HIGH
  Multiple failed login attempts detected (3 occurrences)
  Action: Immediately block source IP, enforce account lockout policy...
```

### Example 2: With AI Enhancement

```python
from src.compressor import SecurityLogCompressor
from src.detector import SecurityLogDetector

# Compress logs first
compressor = SecurityLogCompressor()
compressed = compressor.compress_logs(large_logs)

# Detect with AI
detector = SecurityLogDetector(ai_enabled=True)
anomalies = detector.detect_anomalies(
    logs=large_logs,
    compressed_context=compressed.content
)

# Calculate overall threat
threat_level = detector.calculate_threat_level(anomalies)
print(f"Overall Threat: {threat_level.value}")
```

### Example 3: Full Analysis Pipeline

```python
# Complete workflow
detector = SecurityLogDetector(ai_enabled=False)

# Detect anomalies
anomalies = detector.detect_anomalies(security_logs)

print(f"Found {len(anomalies)} anomalies\n")

# Display by severity
for anomaly in anomalies:
    print(f"[{anomaly.severity.value}] {anomaly.type.value}")
    print(f"  Confidence: {anomaly.confidence:.0%}")
    print(f"  {anomaly.description}")
    
    if anomaly.affected_resources:
        print(f"  Affected: {', '.join(anomaly.affected_resources[:3])}")
    
    print(f"  Recommendation: {anomaly.recommendation}\n")

# Overall assessment
overall = detector.calculate_threat_level(anomalies)
print(f"=== OVERALL THREAT LEVEL: {overall.value} ===")
```

---

## 🔍 Detection Patterns

### Brute Force Detection
- **Pattern:** `(failed|denied|invalid).*(login|authentication|password).*(attempt|tried)`
- **Threshold:** 3+ occurrences
- **Severity:** HIGH
- **Example Match:** "Failed login attempt for user root"

### Suspicious Traffic Detection
- **Pattern:** `(unusual|suspicious|abnormal).*(traffic|connection|outbound)`
- **Threshold:** 1+ occurrence
- **Severity:** CRITICAL
- **Example Match:** "Unusual outbound traffic detected to 198.51.100.77:4444"

### Data Exfiltration Detection
- **Pattern:** `(large|unusual).*(data transfer|upload|exfiltration)`
- **Threshold:** 1+ occurrence
- **Severity:** CRITICAL
- **Example Match:** "Suspicious data transfer of 500MB to external IP"

### Privilege Escalation Detection
- **Pattern:** `(privilege|permission).*(escalat|elevat|gain)|sudo.*(attempt|tried)`
- **Threshold:** 1+ occurrence
- **Severity:** HIGH
- **Example Match:** "User attempted privilege escalation via sudo"

---

## 🎯 Confidence Scoring

Confidence scores indicate detection accuracy:

| Confidence | Meaning |
|-----------|---------|
| 0.95+ | Very high confidence (multiple strong indicators) |
| 0.85-0.94 | High confidence (clear pattern match) |
| 0.70-0.84 | Medium confidence (single pattern match) |
| <0.70 | Lower confidence (partial match) |

Formula: `confidence = min(0.95, 0.7 + (matches * 0.05))`

---

## 🚨 Threat Level Calculation

Overall threat level is calculated based on:

1. **CRITICAL** if:
   - Any CRITICAL severity anomaly detected, OR
   - 2+ HIGH severity anomalies

2. **HIGH** if:
   - 1+ HIGH severity anomaly, OR
   - 3+ MEDIUM severity anomalies

3. **MEDIUM** if:
   - 1+ MEDIUM severity anomaly

4. **LOW** otherwise

---

## 🧪 Testing

Run the module directly to test with sample logs:

```bash
python src/detector.py
```

**Expected Output:**
```
Analyzing security logs...

=== DETECTED ANOMALIES: 2 ===

[1] Suspicious Network Traffic
    Severity: CRITICAL
    Confidence: 75%
    Description: Unusual network traffic patterns detected
    Recommendation: Investigate destination, check firewall rules...
    Affected: 198.51.100.77, 203.0.113.45

[2] Brute Force Attack
    Severity: HIGH
    Confidence: 85%
    Description: Multiple failed login attempts detected (4 occurrences)
    Recommendation: Immediately block source IP...
    Affected: root, 203.0.113.45

=== OVERALL THREAT LEVEL: CRITICAL ===
```

---

## 🔗 Dependencies

```python
from enum import Enum
from dataclasses import dataclass
from dotenv import load_dotenv
from openai import OpenAI  # Optional, for AI detection
```

**Required packages:**
- `python-dotenv==1.0.1`
- `openai==1.54.3` (optional, for AI features)

---

## 📝 Change Log

### 2026-02-01 - Initial Implementation
- Created `SecurityLogDetector` class
- Implemented 8 threat detection patterns
- Added pattern-based detection engine
- Added AI-powered detection (optional)
- Implemented confidence scoring
- Added overall threat level calculation
- Created Anomaly and ThreatLevel data structures
- Added indicator extraction (IPs, users)
- Implemented deduplication logic
- Created comprehensive documentation

---

## 🚀 Next Steps

- [ ] Add more threat patterns (XSS, DoS, etc.)
- [ ] Implement machine learning-based detection
- [ ] Add time-series anomaly detection
- [ ] Create custom rule builder
- [ ] Add threat intelligence feed integration
- [ ] Implement correlation between related events

---

*This detection engine is the intelligence layer of the Security Monitoring Agent.*
