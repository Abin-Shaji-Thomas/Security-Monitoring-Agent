# User Guide

Complete guide to using Security Monitoring Agent for security log analysis.

## 📖 Table of Contents

- [Getting Started](#getting-started)
- [Uploading Logs](#uploading-logs)
- [Analyzing Results](#analyzing-results)
- [Export Options](#export-options)
- [Dark Mode](#dark-mode)
- [Sample Datasets](#sample-datasets)

---

## Getting Started

### Accessing the Dashboard

1. Start the server: `python main.py`
2. Open browser: http://localhost:8001
3. You'll see the main dashboard

### First-Time Setup

1. **Login** with default credentials:
   - Username: `admin`
   - Password: `admin123`

2. **Change Password** (recommended):
   - Click user menu → Settings
   - Update credentials

---

## Uploading Logs

### Method 1: Drag & Drop

1. Drag log file onto the upload zone
2. Supported formats: `.txt`, `.log`, `.json`, `.csv`
3. Maximum size: 10MB
4. File loads automatically

### Method 2: File Picker

1. Click "Browse Files" button
2. Select log file
3. Click "Open"

### Method 3: Paste Text

1. Click in the text area
2. Paste log content (Ctrl+V / Cmd+V)
3. Ready to analyze

### Method 4: Sample Datasets

Select from 10 pre-loaded samples:
- Sample 1: Brute Force Attack
- Sample 2: SQL Injection
- Sample 3: Ransomware
- Sample 4: Insider Threat
- Sample 5: DDoS Attack
- ... and more

---

## Analyzing Results

### Starting Analysis

1. Upload or paste logs
2. Check options:
   - ☑ **Generate PDF Report** - Creates downloadable PDF
   - ☑ **Enable Pattern Learning** - ML-based anomaly detection
3. Click **"Analyze Logs"** button
4. Wait for processing (1-3 seconds)

### Understanding Results

#### Security Score

- **Color-coded status**:
  - 🟢 EXCELLENT (9.0-10.0) - No significant threats
  - 🟡 GOOD (7.0-8.9) - Minor issues found
  - 🟠 MODERATE (5.0-6.9) - Several warnings
  - 🔴 CRITICAL (0-4.9) - Severe threats detected

- **Risk Distribution**: Shows count by severity level

#### Executive Summary

AI-generated overview including:
- Security status
- Number of threats found
- Most common attack types
- Recommended actions

#### Compression Stats

Six key metrics:
1. **Original Tokens** - Before compression
2. **Compressed Tokens** - After optimization
3. **Tokens Saved** - Reduction amount
4. **Percentage Saved** - Compression rate (35-50% typical)
5. **Cost Saved** - Estimated USD savings
6. **Processing Time** - Analysis duration

#### IP Threat Intelligence

For each unique IP found:
- **IP Address** - Source of activity
- **Location** - Country/city
- **Threat Level** - LOW/MEDIUM/HIGH/CRITICAL
- **ISP/Organization** - Network owner

#### Detailed Threats

Each threat shows:
- **Severity** - CRITICAL/HIGH/MEDIUM/LOW
- **Type** - Attack pattern (e.g., "Brute Force")
- **Description** - What happened
- **Timestamp** - When it occurred
- **Source IP** - Origin address
- **Recommendation** - How to respond

---

## Interactive Charts

### Threat Distribution (Doughnut Chart)

- Visual breakdown by severity
- Hover for exact counts
- Color-coded:
  - Red: Critical
  - Orange: High
  - Yellow: Medium
  - Green: Low

### Cost Savings (Bar Chart)

- Compares token usage
- Three bars:
  1. Original tokens
  2. Compressed tokens
  3. Tokens saved
- Shows compression effectiveness

### Security Score (Gauge Chart)

- Semi-circle gauge (0-10)
- Color matches status
- Visual security health indicator

---

## Export Options

### CSV Export

- Click **"Export CSV"** button
- Downloads: `security_analysis.csv`
- Contains: All threats in tabular format
- Best for: Excel analysis, data processing

### JSON Export

- Click **"Export JSON"** button
- Downloads: `security_analysis.json`
- Contains: Complete analysis data + metadata
- Best for: API integration, automation

### Excel Export

- Click **"Export Excel"** button
- Downloads: `security_analysis.xlsx`
- Contains 3 sheets:
  1. **Summary** - Overview metrics
  2. **Threats** - Detailed threat list
  3. **IP Intelligence** - Geographic data
- Best for: Professional reports, presentations

### PDF Report

- Enable "Generate PDF Report" before analysis
- Click **"Download PDF"** after analysis
- Contains: Complete formatted report
- Best for: Sharing, documentation

---

## Dark Mode

### Enable Dark Mode

1. Click 🌙 toggle in top-right corner
2. Interface switches to dark theme
3. Preference saved automatically

### Features

- **Persistence**: Remembers your choice
- **Eye-friendly**: Reduces strain in low light
- **Professional**: Clean dark aesthetics

---

## Sample Datasets

### Available Samples

1. **Brute Force Attack** (40 lines)
   - Multiple failed SSH login attempts
   - Account lockout trigger
   - IP blocking action

2. **SQL Injection** (36 lines)
   - Database query manipulation
   - UNION SELECT attacks
   - WAF blocking

3. **Ransomware** (41 lines)
   - Mass file encryption
   - Backup deletion
   - Ransom note creation

4. **Insider Threat**
   - Data exfiltration
   - USB transfer
   - After-hours access

5. **DDoS Attack**
   - Traffic spike
   - Resource exhaustion
   - Service disruption

6. **Privilege Escalation**
   - Unauthorized sudo
   - Credential dumping
   - Admin access gained

7. **C2 Communication**
   - Beacon detected
   - Encrypted channel
   - Payload download

8. **Phishing**
   - Credential submission
   - Fake login page
   - Account compromise

9. **Cryptomining**
   - High CPU usage
   - Mining pool connection
   - Unauthorized software

10. **Zero-Day APT**
    - Advanced exploit
    - Lateral movement
    - Data staging

### Using Samples

1. Open dropdown menu
2. Select desired sample
3. Logs load automatically
4. Click "Analyze Logs"

---

## Best Practices

### Log Preparation

- **Clean format**: One event per line preferred
- **Include timestamps**: Better analysis accuracy
- **Keep context**: Don't over-filter before upload
- **Size limits**: Split large files (10MB max)

### Analysis Options

- **Pattern Learning**: Enable for unknown threats
- **PDF Generation**: Only when needed (slower)
- **Regular Analysis**: Check logs daily/weekly

### Reviewing Results

1. Check **Security Score** first
2. Read **Executive Summary**
3. Review **Critical threats** immediately
4. Investigate **IP addresses**
5. Export results for records

---

## Keyboard Shortcuts

- `Ctrl+V` / `Cmd+V` - Paste logs
- `Ctrl+Enter` - Start analysis
- `Esc` - Clear results

---

## Common Workflows

### Daily Security Check

1. Upload today's logs
2. Enable pattern learning
3. Analyze logs
4. Review critical threats
5. Export CSV for records

### Incident Response

1. Upload suspicious logs
2. Generate PDF report
3. Review all threats
4. Check IP intelligence
5. Share PDF with team

### Compliance Audit

1. Collect period logs
2. Analyze with pattern learning
3. Export Excel report
4. Review all incidents
5. Document in report

---

## Tips & Tricks

- **Large Files**: Split into chunks for faster processing
- **Regular Patterns**: Use pattern learning to improve detection
- **Export Early**: Save results before starting new analysis
- **Dark Mode**: Better for long sessions
- **Samples**: Test features with pre-loaded datasets

---

## Getting Help

- **In-App**: Hover over ℹ️ icons for tooltips
- **Documentation**: Check [docs/](../)
- **Support**: [GitHub Issues](https://github.com/yourusername/Security-Monitoring-Agent/issues)

---

## Next Steps

- [Authentication Guide](AUTHENTICATION.md) - User management
- [Export Guide](EXPORT.md) - Advanced export options
- [API Documentation](../api/API.md) - Automate analysis
