# Security Monitoring Agent v2.0

> AI-Powered Security Log Analysis with Compression, Threat Intelligence, and Advanced Reporting

## What It Does

1. **Compresses logs** using ScaleDown API (30-70% token reduction)
2. **Detects threats** with 8 pattern types + AI analysis
3. **Analyzes IPs** with geolocation & threat intelligence
4. **Calculates risk scores** (0-100) for each threat
5. **Generates insights** with AI-powered summaries
6. **Tracks history** in SQLite database with trends
7. **Creates PDF reports** for compliance & executive review
8. **Learns patterns** to detect anomalies from baseline

## Quick Start

```bash
# Install
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Configure .env file
SCALEDOWN_API_KEY=your_key_here
OPENAI_API_KEY=sk-...  # Optional for AI insights

# Run
python main.py

# Open browser
http://127.0.0.1:8001
```

## Core Features

✅ **30-70% log compression** - ScaleDown REST API integration  
✅ **8 threat detection patterns** - Brute Force, SQL Injection, Malware, etc.  
✅ **Cost savings calculator** - Real-time USD savings display  
✅ **Interactive web dashboard** - Beautiful gradient purple UI  
✅ **REST API** - Full FastAPI backend with docs  
✅ **1-3 second response time** - Optimized performance  

## NEW: Advanced Features v2.0

### 🌍 IP Threat Intelligence
- Automatic IP extraction & geolocation
- Threat level assessment per IP
- Geographic attack source mapping
- Country/ISP identification

### 📊 Risk Scoring System
- Comprehensive 0-100 threat scores
- Multi-factor risk calculation
- Overall security health score
- Risk level categorization (CRITICAL/HIGH/MEDIUM/LOW)

### 📈 Historical Dashboard
- SQLite database with all analysis history
- Threat trends over time
- Most attacked resources leaderboard
- Dangerous IP tracking

### 🤖 AI-Powered Insights
- Executive summaries in natural language
- Incident response plan generation
- Attack pattern detection
- Coordinated attack analysis

### 📄 PDF Report Generator
- Professional branded reports
- Executive summary + technical details
- Compliance-ready format
- Color-coded severity tables

### 🔄 Pattern Learning
- Learns normal behavior baseline
- Detects deviations from norm
- Adaptive anomaly detection
- Reduces false positives over time

[→ See Full Advanced Features Documentation](docs/ADVANCED_FEATURES.md)

## Tech Stack

- **Backend**: Python 3.14 + FastAPI + Uvicorn
- **Compression**: ScaleDown REST API
- **Database**: SQLite (threat history)
- **AI**: OpenAI GPT (optional)
- **Reports**: ReportLab PDF generation
- **Frontend**: Pure HTML/CSS/JS (no build tools)

## Documentation

📚 [Documentation Hub](docs/INDEX.md)  
🚀 [Setup Guide](docs/SETUP_GUIDE.md)  
🔌 [API Reference](docs/API.md)  
⚡ [Advanced Features](docs/ADVANCED_FEATURES.md)  
📁 [Project Structure](docs/PROJECT_STRUCTURE.md)  

## Project Structure

```
src/
  compressor.py         # ScaleDown integration
  detector.py           # Pattern-based threat detection
  ip_intelligence.py    # IP geolocation & threat intel
  scoring.py            # Risk scoring engine
  ai_insights.py        # AI-powered analysis
  history.py            # SQLite database management
  pdf_report.py         # PDF generation
  pattern_learning.py   # Anomaly detection via learning
frontend/
  index.html            # Web dashboard UI
main.py                 # FastAPI application entry point
data/                   # Database & baseline storage
reports/                # Generated PDF reports
```

## Threat Types Detected

1. Brute Force Attack
2. Unauthorized Access
3. Suspicious Network Traffic
4. Data Exfiltration
5. Privilege Escalation
6. SQL Injection Attempt
7. Malware Activity
8. Failed Authentication

## API Endpoints

### Core Analysis
- `POST /analyze` - Analyze logs with all features
- `GET /health` - Health check with feature list

### Historical Analysis
- `GET /history/trends?days=7` - Get threat trends
- `GET /history/statistics` - Overall statistics
- `GET /history/recent?limit=10` - Recent analyses

### Pattern Learning
- `GET /baseline/summary` - Learned baseline info
- `POST /baseline/learn` - Train from clean logs

## Cost Savings Example

**Input**: 100,000 tokens  
**Output**: 40,000 tokens  
**Savings**: 60% = $0.012/request @ GPT-4o-mini pricing

## Example Response (Enhanced)

```json
{
  "success": true,
  "threats": [
    {
      "type": "Brute Force Attack",
      "severity": "HIGH",
      "risk_score": 85.5,
      "source_ip": "45.142.212.33",
      "country": "Russia",
      "description": "Multiple failed login attempts",
      "confidence": 0.95
    }
  ],
  "overall_security": {
    "overall_score": 42.5,
    "health_status": "FAIR",
    "risk_distribution": {
      "CRITICAL": 2,
      "HIGH": 3
    }
  },
  "ip_intelligence": {
    "total_ips": 5,
    "threat_ips": [
      {
        "ip": "45.142.212.33",
        "country": "Russia",
        "threat_level": "HIGH"
      }
    ]
  },
  "executive_summary": "AI-generated security summary...",
  "pdf_report_path": "reports/security_report_20260201_143015.pdf"
}
```

## Status

✅ **FULLY OPERATIONAL v2.0**
- All 6 advanced features working
- Server tested and validated
- ScaleDown integrated
- Threat detection active
- IP intelligence operational
- Risk scoring functional
- History tracking enabled
- PDF generation ready
- Pattern learning available

## GitHub Repository

🔗 https://github.com/Abin-Shaji-Thomas/Security-Monitoring-Agent

## License

MIT License - See LICENSE file for details

---

Built with ❤️ for cybersecurity professionals
