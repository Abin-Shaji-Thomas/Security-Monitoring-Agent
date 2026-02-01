# Quick Setup Guide

**Last Updated:** February 1, 2026

---

## ⚡ Quick Start (5 minutes)

### 1. Clone Repository

```bash
git clone https://github.com/Abin-Shaji-Thomas/Security-Monitoring-Agent.git
cd Security-Monitoring-Agent
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If `scaledown` installation fails, install core dependencies first:
```bash
pip install fastapi uvicorn python-dotenv openai pydantic requests
```

### 4. Configure Environment

Create `.env` file:
```bash
# Copy template
cp .env.example .env

# Edit with your keys
SCALEDOWN_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here_optional
```

### 5. Run Application

```bash
python app.py
```

Application will start at: **http://localhost:8000**

---

## 🧪 Test the API

### Option 1: Browser

Visit: `http://localhost:8000`

### Option 2: API Docs

Visit: `http://localhost:8000/docs`

### Option 3: cURL

```bash
curl http://localhost:8000/health
```

---

##  Troubleshooting

### Issue: ModuleNotFoundError: No module named 'scaledown'

**Solution:**
```bash
# Install from requirements
pip install scaledown

# Or with extras
pip install "scaledown[haste,semantic]"
```

### Issue: API Key Not Found

**Solution:**
- Check `.env` file exists
- Verify `SCALEDOWN_API_KEY` is set
- Restart the application

### Issue: Port 8000 Already in Use

**Solution:**
```bash
# Use different port
PORT=3000 python app.py
```

---

## 📝 Next Steps

1. ✅ Application running
2. Test with sample logs (`logs/sample_logs.txt`)
3. Try the `/api/analyze` endpoint
4. Build frontend dashboard
5. Deploy to Vercel

---

*For detailed setup instructions, see the [main README](../README.md).*
