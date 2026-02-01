# Advanced Features Documentation

## Overview

Security Monitoring Agent v2.0 includes 6 powerful advanced features that enhance threat detection, analysis, and reporting capabilities.

---

## 1. 🌍 IP Threat Intelligence & Geolocation

### Description
Automatically analyzes IP addresses from logs, providing geolocation data and threat intelligence.

### Features
- **Automatic IP Extraction**: Identifies all IP addresses in log files
- **Geolocation Lookup**: Determines country, city, ISP for each IP
- **Threat Assessment**: Checks IPs against threat databases
- **Threat Mapping**: Visualizes attack sources geographically

### Usage

The IP intelligence module runs automatically during analysis. No additional configuration required.

```python
# API Response includes IP intelligence data
{
  "ip_intelligence": {
    "total_ips": 5,
    "threat_ips": [
      {
        "ip": "45.142.212.33",
        "country": "Russia",
        "city": "Moscow",
        "threat_level": "HIGH",
        "threat_types": ["Brute Force", "Scanning"]
      }
    ],
    "safe_ips": ["203.0.113.50"],
    "countries": {
      "Russia": 2,
      "United States": 3
    },
    "threat_map": [
      {
        "lat": 55.7558,
        "lon": 37.6173,
        "ip": "45.142.212.33",
        "country": "Russia",
        "threat_level": "HIGH"
      }
    ]
  }
}
```

### Data Sources
- **Geolocation**: ip-api.com (free, no key required)
- **Threat Intel**: Basic heuristics (upgradeable with AbuseIPDB API key)

---

## 2. 📊 Threat Severity Scoring System

### Description
Calculates comprehensive risk scores (0-100) for each threat based on multiple factors.

### Scoring Factors

1. **Base Score**: Threat type severity (e.g., Data Exfiltration = 95)
2. **Frequency Multiplier**: Attack rate over time
3. **Target Sensitivity**: Resource importance (admin, database = higher)
4. **Sophistication**: Attack complexity
5. **Confidence**: Detection certainty

### Risk Levels

- **CRITICAL**: 80-100 - Immediate action required
- **HIGH**: 60-79 - Priority response needed
- **MEDIUM**: 40-59 - Review and address
- **LOW**: 20-39 - Monitor
- **MINIMAL**: 0-19 - Informational

### Example Output

```json
{
  "overall_security": {
    "overall_score": 42.5,
    "health_status": "FAIR",
    "risk_distribution": {
      "CRITICAL": 2,
      "HIGH": 3,
      "MEDIUM": 1
    },
    "highest_risk": {
      "type": "SQL Injection Attempt",
      "score": 95.5,
      "level": "CRITICAL"
    },
    "total_threats": 6,
    "average_threat_score": 57.5
  }
}
```

### Individual Threat Scores

Each threat now includes a `risk_score` field:

```json
{
  "type": "Brute Force Attack",
  "severity": "HIGH",
  "risk_score": 85.5,
  "description": "Multiple failed login attempts detected"
}
```

---

## 3. 📈 Historical Threat Dashboard

### Description
SQLite database storing all analysis history with trend analysis and statistics.

### Stored Data

- Analysis sessions with timestamps
- All detected threats
- IP attack history
- Compression metrics
- Security scores over time

### API Endpoints

#### Get Threat Trends
```bash
GET /history/trends?days=7
```

Response:
```json
{
  "daily_counts": [
    {"date": "2026-01-25", "count": 15},
    {"date": "2026-01-26", "count": 22}
  ],
  "threat_types": [
    {"type": "Brute Force Attack", "count": 45},
    {"type": "SQL Injection", "count": 12}
  ],
  "top_targets": [
    {"resource": "admin", "count": 23},
    {"resource": "database", "count": 18}
  ],
  "dangerous_ips": [
    {
      "ip": "45.142.212.33",
      "country": "Russia",
      "incidents": 15,
      "threat_level": "CRITICAL",
      "last_seen": "2026-02-01T14:30:00"
    }
  ]
}
```

#### Get Overall Statistics
```bash
GET /history/statistics
```

Response:
```json
{
  "total_analyses": 150,
  "total_threats": 487,
  "average_threats_per_session": 3.25,
  "most_common_threat": "Brute Force Attack",
  "unique_malicious_ips": 78
}
```

#### Get Recent Analyses
```bash
GET /history/recent?limit=10
```

### Database Location
`data/threat_history.db`

---

## 4. 🤖 AI-Powered Log Insights

### Description
Uses AI (OpenAI GPT) to generate natural language summaries and actionable recommendations.

### Features

#### Executive Summary
Natural language summary of security analysis:

```
"Security analysis reveals 6 threats detected in the last hour, 
with a concerning pattern of brute force attempts from Russian IPs 
targeting admin accounts. Overall security score: 42/100 (FAIR). 
Immediate attention required for privilege escalation attempts. 
Recommend implementing rate limiting and reviewing admin access logs."
```

#### Incident Response Plans
AI-generated step-by-step response procedures for each threat:

```
1. Isolate affected systems immediately
2. Review and block source IPs (45.142.212.33, 203.0.113.50)
3. Notify security team and management
4. Implement account lockout policies
5. Enable multi-factor authentication
6. Review password policies
```

#### Attack Pattern Analysis
Detects coordinated attack campaigns:

```json
{
  "is_coordinated": true,
  "confidence": 85,
  "attack_chain": "Initial brute force → privilege escalation → data exfiltration",
  "attack_goal": "Data theft from database servers"
}
```

### Configuration

Set OpenAI API key in `.env`:
```
OPENAI_API_KEY=sk-...
```

If no API key is provided, system uses intelligent fallback summaries.

---

## 5. 📄 Professional PDF Report Generator

### Description
Generates branded, professional PDF security reports for compliance and executive review.

### Report Contents

1. **Title Page** with generation timestamp
2. **Executive Summary** (AI-powered or basic)
3. **Security Overview** table with key metrics
4. **Detailed Threat Analysis** with risk scores
5. **IP Threat Intelligence** with malicious IP tables
6. **Actionable Recommendations**

### Usage

Enable PDF generation in API request:

```json
{
  "logs": "...",
  "generate_pdf": true
}
```

Response includes path:
```json
{
  "pdf_report_path": "reports/security_report_20260201_143015.pdf"
}
```

### Report Features

- Color-coded severity levels
- Professional formatting with tables and sections
- Charts showing risk distribution
- Geographic threat mapping
- Compliance-ready format

### Requirements
```bash
pip install reportlab
```

### Output Location
`reports/` directory (auto-created)

---

## 6. 🔄 Log Pattern Learning

### Description
Machine learning-based anomaly detection that learns "normal" behavior patterns and flags deviations.

### How It Works

1. **Baseline Learning**: Feed clean logs to establish normal patterns
2. **Pattern Storage**: Stores learned patterns in JSON baseline
3. **Anomaly Detection**: Compares new logs against baseline
4. **Adaptive Learning**: Continuously updates baseline with clean data

### Learned Patterns

- User activity patterns (normal vs rare users)
- IP address frequency (trusted vs new IPs)
- Time-based patterns (normal activity hours)
- Resource access patterns (typical vs unusual paths)
- Log level distribution

### API Endpoints

#### Learn from Clean Logs
```bash
POST /baseline/learn
{
  "logs": "...",
  "is_clean": true
}
```

#### Get Baseline Summary
```bash
GET /baseline/summary
```

Response:
```json
{
  "version": "1.0",
  "last_updated": "2026-02-01T14:30:00",
  "total_logs_analyzed": 5000,
  "unique_users": 25,
  "unique_ips": 150,
  "unique_resources": 89,
  "log_type_distribution": {
    "INFO": 3500,
    "WARNING": 1200,
    "ERROR": 250,
    "CRITICAL": 50
  }
}
```

### Usage in Analysis

Enable pattern anomalies in request:

```json
{
  "logs": "...",
  "learn_patterns": true
}
```

Response includes pattern-based anomalies:
```json
{
  "pattern_anomalies": [
    {
      "type": "Unknown User",
      "description": "Never before seen user \"hacker123\"",
      "line": 15,
      "confidence": 0.85,
      "recommendation": "Investigate new user account activity"
    },
    {
      "type": "New IP Address",
      "description": "Never before seen IP: 45.142.212.33",
      "line": 22,
      "confidence": 0.75,
      "recommendation": "Check IP reputation and geolocation"
    }
  ]
}
```

### Baseline Storage
`data/pattern_baseline.json`

### Best Practices

1. Start with 100+ lines of verified clean logs
2. Use `is_clean=true` only for threat-free logs
3. Update baseline regularly with normal operations
4. Review pattern anomalies alongside threat detection

---

## Combined Example

Full analysis request using all features:

```bash
POST /analyze
{
  "logs": "...",
  "prompt": "Identify security threats",
  "generate_pdf": true,
  "learn_patterns": true
}
```

Response structure:
```json
{
  "success": true,
  "compressed_context": "...",
  "ai_response": "...",
  "threats": [
    {
      "type": "Brute Force Attack",
      "severity": "HIGH",
      "risk_score": 85.5,
      "source_ip": "45.142.212.33",
      "country": "Russia",
      "description": "...",
      "recommendation": "...",
      "confidence": 0.95,
      "affected": ["admin", "root"]
    }
  ],
  "compression_stats": {...},
  "cost_savings": {...},
  "overall_security": {
    "overall_score": 42.5,
    "health_status": "FAIR",
    "risk_distribution": {...},
    "highest_risk": {...}
  },
  "ip_intelligence": {
    "total_ips": 5,
    "threat_ips": [...],
    "threat_map": [...]
  },
  "executive_summary": "AI-generated summary...",
  "pdf_report_path": "reports/security_report_20260201_143015.pdf",
  "pattern_anomalies": [...]
}
```

---

## Performance Impact

All features are optimized for minimal performance impact:

- IP lookups: Cached (1-hour TTL)
- Database operations: Indexed for speed
- PDF generation: Optional, on-demand only
- Pattern learning: Lightweight regex patterns
- AI insights: Optional, falls back to basic summaries

---

## Configuration

### Environment Variables

```bash
# Required
SCALEDOWN_API_KEY=your_key_here

# Optional enhancements
OPENAI_API_KEY=sk-...          # For AI insights
ABUSEIPDB_API_KEY=your_key     # For enhanced IP threat intel
```

### Feature Toggles

All features are opt-in via API parameters:
- `generate_pdf`: Create PDF reports
- `learn_patterns`: Enable pattern-based anomaly detection

---

## Troubleshooting

### PDF Generation Fails
```bash
pip install reportlab
```

### AI Insights Not Working
Check `OPENAI_API_KEY` in `.env`. System will use fallback summaries if not configured.

### Database Lock Errors
SQLite is single-writer. High-traffic deployments should use PostgreSQL (future enhancement).

### Pattern Learning Insufficient
Need 100+ clean log lines for reliable baseline. Check:
```bash
GET /baseline/summary
```

---

## Future Enhancements

- Real-time WebSocket updates
- Interactive threat map visualization
- Custom alert rules engine
- Multi-workspace support
- PostgreSQL support for high traffic
- Integration with SIEM platforms

---

## Support

For issues or questions about advanced features:
- GitHub Issues: https://github.com/Abin-Shaji-Thomas/Security-Monitoring-Agent/issues
- Documentation: https://github.com/Abin-Shaji-Thomas/Security-Monitoring-Agent/tree/main/docs
