# Setup Guide

## Quick Start (5 minutes)

### 1. Install
\\ash
git clone https://github.com/Abin-Shaji-Thomas/Security-Monitoring-Agent.git
cd Security-Monitoring-Agent
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
\
### 2. Configure
Create .env file:
\SCALEDOWN_API_KEY=your_key_here
\
### 3. Run
\\ash
python main.py
\
### 4. Open
http://127.0.0.1:8001

## Dependencies

Only 5 core packages:
- fastapi - Web framework
- uvicorn - Server  
- requests - HTTP client
- python-dotenv - Environment vars
- pydantic - Data validation

## Troubleshooting

**Port busy?** Change port in main.py line 133
**API key error?** Check .env file exists
**Import error?** Activate virtual environment

That is it!
