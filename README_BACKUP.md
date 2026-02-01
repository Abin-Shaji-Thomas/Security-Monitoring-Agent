#  Security Monitoring Agent

> Compress security logs + Detect threats + Save costs

## What It Does

1. Compresses security logs using ScaleDown API (30-70% reduction)
2. Detects 8 types of threats (Brute Force, SQL Injection, etc.)
3. Shows real-time cost savings in USD
4. Beautiful web dashboard

## Quick Start

\\ash
# Install
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt

# Configure .env file
SCALEDOWN_API_KEY=your_key_here

# Run
python main.py

# Open browser
http://127.0.0.1:8001
\
## Features

 30-70% token compression
 8 threat detection patterns  
 Cost savings calculator
 Interactive web UI
 REST API
 1-3 second response time

## Tech Stack

- Python + FastAPI + Uvicorn
- ScaleDown REST API
- Pattern matching + AI analysis
- Pure HTML/CSS/JS frontend

## Documentation

 [Full Docs](docs/INDEX.md)
 [Setup Guide](docs/SETUP_GUIDE.md)
 [API Reference](docs/API.md)

## Project Structure

\src/
  compressor.py    # ScaleDown integration
  detector.py      # Threat detection
frontend/
  index.html       # Web dashboard
main.py           # Entry point
\
## Threat Types Detected

1. Brute Force Attack
2. Unauthorized Access
3. Suspicious Traffic
4. Data Exfiltration
5. Privilege Escalation
6. SQL Injection
7. Malware Activity
8. Failed Authentication

## Cost Savings Example

100,000 tokens  40,000 tokens = 60% saved = /request @ GPT-4o-mini pricing

## Status

 **WORKING**
- Server operational
- ScaleDown integrated
- Threat detection active
- UI tested

Built with  for cybersecurity
