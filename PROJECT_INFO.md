# Security Monitoring Agent v2.0 - Technical Documentation

## 🔍 ScaleDown API Integration

### What is ScaleDown?
ScaleDown is an AI compression API that reduces the token count of security logs before sending them to LLM models (like GPT-4) for analysis. This dramatically reduces costs while maintaining analysis quality.

### How It Works in Our Project:

**1. Log Compression Flow:**
```
Raw Security Logs (100+ lines)
    ↓
ScaleDown API (https://api.scaledown.xyz/compress/raw/)
    ↓
Compressed Context (50% fewer tokens)
    ↓
GPT-4o-mini Analysis
    ↓
Security Threats Detected
```

**2. Implementation Location:**
- **File:** `src/compressor.py`
- **Class:** `SecurityLogCompressor`
- **API Key:** Loaded from `.env` file (`SCALEDOWN_API_KEY`)

**3. Code Workflow:**
```python
# Step 1: Initialize compressor with API key
compressor = SecurityLogCompressor()

# Step 2: Send logs to ScaleDown API
result = compressor.compress_logs(logs, prompt="Analyze security threats")

# Step 3: Get compressed context and AI analysis
compressed_context = result['compressed_context']
ai_response = result['content']

# Step 4: Calculate savings
stats = compressor.get_compression_stats(result)
# Returns: original_tokens, compressed_tokens, tokens_saved, savings_percent
```

**4. Cost Savings Example:**
- **Original Logs:** 1000 tokens
- **After Compression:** 500 tokens (50% reduction)
- **Cost Saved:** $0.0075 per 1K tokens
- **Annual Savings:** ~$27,375 for 1M daily analyses

**5. API Configuration:**
```env
SCALEDOWN_API_KEY=Mi5T2Bah347Zwm219z4g51u8kFCliV4k9qPiB39q
TARGET_MODEL=gpt-4o-mini
```

**6. Response Format:**
```json
{
  "content": "AI analysis of threats...",
  "compressed_context": "Compressed logs...",
  "usage": {
    "prompt_tokens_uncompressed": 1000,
    "prompt_tokens": 500
  },
  "latency_ms": 1500
}
```

---

## 🏗️ Project Architecture

### Directory Structure:
```
Security-Monitoring-Agent/
├── main.py                      # FastAPI server entry point
├── frontend/
│   └── index.html              # Web UI with 10 sample datasets
├── src/
│   ├── compressor.py           # ScaleDown API integration
│   ├── detector.py             # Pattern-based threat detection
│   ├── ip_intelligence.py      # IP geolocation & threat intel
│   ├── scoring.py              # Risk scoring engine (0-100)
│   ├── ai_insights.py          # AI executive summaries
│   ├── history.py              # SQLite historical database
│   ├── pdf_report.py           # PDF generation (ReportLab)
│   └── pattern_learning.py     # Behavioral baseline learning
├── logs/
│   ├── sample_01_brute_force.txt
│   ├── sample_02_sql_injection.txt
│   ├── sample_03_ransomware.txt
│   ├── sample_04_insider_threat.txt
│   ├── sample_05_ddos_attack.txt
│   ├── sample_06_privilege_escalation.txt
│   ├── sample_07_c2_communication.txt
│   ├── sample_08_phishing.txt
│   ├── sample_09_cryptomining.txt
│   ├── sample_10_zero_day_apt.txt
│   └── README.md
├── reports/                     # Generated PDF reports
├── data/
│   ├── threat_history.db       # SQLite database
│   └── pattern_baseline.json   # Learned patterns
├── .env                         # API keys (DO NOT COMMIT)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🔧 Core Features

### 1. **Log Compression** (ScaleDown API)
- Reduces token count by 40-60%
- Maintains semantic meaning
- Saves ~$0.007 per 1K tokens
- Average latency: 1500-2000ms

### 2. **Threat Detection** (Pattern-Based + AI)
- **13 Detection Patterns:**
  1. Brute Force Attacks
  2. SQL Injection
  3. Ransomware
  4. Insider Threat
  5. DDoS Attacks
  6. Privilege Escalation
  7. C2 Communication
  8. Phishing
  9. Cryptomining
  10. Zero-Day APT
  11. Data Exfiltration
  12. Unauthorized Access
  13. Suspicious Processes

### 3. **IP Intelligence**
- Geolocation lookup (ip-api.com)
- Threat level assessment
- Country identification
- Optional AbuseIPDB integration

### 4. **Risk Scoring**
- 0-100 numerical score per threat
- Factors: frequency, severity, target sensitivity, sophistication
- Risk levels: LOW, MEDIUM, HIGH, CRITICAL

### 5. **AI Insights**
- Executive summaries (GPT-powered)
- Incident response plans
- Attack pattern analysis
- Fallback mode (no OpenAI key required)

### 6. **Historical Analysis**
- SQLite database tracking
- Threat trends over time
- Statistics dashboard
- Pattern recognition

### 7. **PDF Reports**
- Professional multi-page reports
- Color-coded threat tables
- IP intelligence sections
- Downloadable via web UI

### 8. **Pattern Learning**
- Baseline behavioral analysis
- Anomaly detection
- User/IP/resource frequency tracking
- JSON-based storage

---

## 🚀 API Endpoints

### Analysis
- **POST** `/analyze` - Analyze security logs
  - Body: `{ logs, prompt, generate_pdf, learn_patterns }`
  - Returns: threats, scores, IP intel, AI summary, PDF path

### Downloads
- **GET** `/download/report/{filename}` - Download PDF report

### Historical Data
- **GET** `/history/trends?days=7` - Get threat trends
- **GET** `/history/statistics` - Overall statistics
- **GET** `/history/recent?limit=10` - Recent analyses

### Pattern Learning
- **GET** `/baseline/summary` - Get learned baseline
- **POST** `/baseline/learn` - Learn from clean logs

### Health
- **GET** `/health` - Service health check

---

## 📊 Sample Datasets

All 10 samples are stored in `logs/` folder and embedded in frontend JavaScript:

| Sample | File | Key Threats |
|--------|------|-------------|
| 1 | sample_01_brute_force.txt | Failed logins, SSH brute force |
| 2 | sample_02_sql_injection.txt | SQL injection, database attacks |
| 3 | sample_03_ransomware.txt | File encryption, backup deletion |
| 4 | sample_04_insider_threat.txt | Data export, USB transfer |
| 5 | sample_05_ddos_attack.txt | Traffic spike, resource exhaustion |
| 6 | sample_06_privilege_escalation.txt | Sudo abuse, credential dumping |
| 7 | sample_07_c2_communication.txt | Beacon traffic, remote execution |
| 8 | sample_08_phishing.txt | Fake login, credential theft |
| 9 | sample_09_cryptomining.txt | CPU spike, mining pool |
| 10 | sample_10_zero_day_apt.txt | Zero-day, lateral movement |

---

## 🔐 Environment Variables

Required in `.env` file:
```env
# ScaleDown API (REQUIRED)
SCALEDOWN_API_KEY=Mi5T2Bah347Zwm219z4g51u8kFCliV4k9qPiB39q
TARGET_MODEL=gpt-4o-mini

# Optional: OpenAI for AI Insights
OPENAI_API_KEY=your_key_here

# Optional: AbuseIPDB for enhanced IP intel
ABUSEIPDB_API_KEY=your_key_here
```

---

## 🎯 Testing the Application

### 1. Start Server:
```bash
python main.py
# or
.venv\Scripts\python.exe main.py
```

### 2. Access Web UI:
```
http://127.0.0.1:8001
```

### 3. Test Samples:
1. Select "Sample 1: Brute Force Attack" from dropdown
2. Check "Generate PDF Report"
3. Click "Analyze Logs"
4. Verify threats detected
5. Click "Download PDF Report"

### 4. Expected Results:
- ✅ Security score calculated (0-100)
- ✅ Threats detected with risk scores
- ✅ IP intelligence shown
- ✅ Executive summary generated
- ✅ Cost savings displayed
- ✅ PDF downloadable

---

## 📦 Dependencies

Install via `pip install -r requirements.txt`:

```txt
fastapi==0.115.0
uvicorn==0.32.0
requests==2.32.3
python-dotenv==1.0.1
scaledown==0.1.0
reportlab==4.4.9
openai==1.54.3 (optional)
```

---

## 🐛 Troubleshooting

### Issue: No threats detected
**Solution:** Updated detection patterns in `src/detector.py` to match all 10 sample types

### Issue: PDF not downloading
**Solution:** Added `/download/report/{filename}` endpoint with FileResponse

### Issue: Dropdown not loading data
**Solution:** Fixed JavaScript to use `parseInt()` for sample ID

### Issue: ScaleDown API error
**Solution:** Check `.env` has valid `SCALEDOWN_API_KEY`

---

## 🔮 Future Enhancements

1. Real-time log streaming
2. Email/Slack notifications
3. Multi-tenant support
4. Custom detection rules
5. Integration with SIEM systems
6. Machine learning-based detection
7. API rate limiting
8. User authentication

---

## 📝 License

MIT License - See LICENSE file for details

## 👨‍💻 Developer

Created for cybersecurity log analysis and threat detection demonstrations.

**Version:** 2.0.0  
**Last Updated:** February 1, 2026
