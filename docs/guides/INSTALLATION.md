# Installation Guide

Complete guide for installing Security Monitoring Agent on various platforms.

##📋 Prerequisites

Before installation, ensure you have:

- **Python 3.8+** (Python 3.10+ recommended)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **ScaleDown API Key** ([Get one here](https://scaledown.xyz))
- **4GB RAM** minimum
- **500MB disk space**

---

## 🪟 Windows Installation

### 1. Install Python

Download from [python.org](https://www.python.org/downloads/) and ensure "Add Python to PATH" is checked.

### 2. Clone Repository

```cmd
git clone https://github.com/yourusername/Security-Monitoring-Agent.git
cd Security-Monitoring-Agent
```

### 3. Create Virtual Environment

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install Dependencies

```cmd
pip install -r requirements.txt
```

### 5. Configure Environment

```cmd
copy .env.example .env
notepad .env
```

Add your ScaleDown API key:
```
SCALEDOWN_API_KEY=your_key_here
```

### 6. Run Server

```cmd
python main.py
```

Access at: http://localhost:8001

---

## 🐧 Linux Installation

### 1. Install Python (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```

### 2. Clone Repository

```bash
git clone https://github.com/yourusername/Security-Monitoring-Agent.git
cd Security-Monitoring-Agent
```

### 3. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment

```bash
cp .env.example .env
nano .env
```

Add your ScaleDown API key.

### 6. Run Server

```bash
python main.py
```

---

## 🍎 macOS Installation

### 1. Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install Python

```bash
brew install python3 git
```

### 3. Clone and Setup

```bash
git clone https://github.com/yourusername/Security-Monitoring-Agent.git
cd Security-Monitoring-Agent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure and Run

```bash
cp .env.example .env
# Edit .env with your API key
python main.py
```

---

## 🐳 Docker Installation (Coming Soon)

```bash
docker pull yourusername/security-monitoring-agent
docker run -p 8001:8001 -e SCALEDOWN_API_KEY=your_key security-monitoring-agent
```

---

## 🔧 Configuration Options

### Environment Variables (.env)

```env
# Required
SCALEDOWN_API_KEY=your_scaledown_api_key

# Optional
OPENAI_API_KEY=your_openai_key  # For enhanced AI insights
HOST=0.0.0.0                     # Server host
PORT=8001                        # Server port
TARGET_MODEL=gpt-4o              # AI model
```

### Database Configuration

- SQLite databases are created automatically
- Location: `threat_history.db`, `users.db`
- No additional configuration needed

---

## ✅ Verify Installation

### 1. Check Server Health

```bash
curl http://localhost:8001/health
```

Expected response:
```json
{"status":"healthy","version":"2.0.0"}
```

### 2. Access Web Interface

Open browser: http://localhost:8001

### 3. Test Login

Use default credentials:
- Username: `admin`
- Password: `admin123`

**⚠️ Change these immediately!**

### 4. Run Test Suite

```bash
python test.py
```

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Find process using port 8001
lsof -i :8001  # Linux/macOS
netstat -ano | findstr :8001  # Windows

# Kill the process or change PORT in .env
```

### Python Version Issues

```bash
# Check Python version
python --version

# Should be 3.8 or higher
```

### Permission Errors (Linux)

```bash
# Install to user directory
pip install --user -r requirements.txt
```

### Virtual Environment Not Activating

```bash
# Windows PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then retry activation
```

### Missing Dependencies

```bash
# Reinstall all dependencies
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

---

## 📦 Production Deployment

See [Deployment Guide](DEPLOYMENT.md) for:
- Nginx reverse proxy setup
- SSL certificate configuration
- Systemd service configuration
- Auto-restart on failure
- Log rotation
- Monitoring setup

---

## 🆘 Getting Help

- **Documentation**: Check [docs/](../docs/)
- **Issues**: [GitHub Issues](https://github.com/yourusername/Security-Monitoring-Agent/issues)
- **Community**: [Discussions](https://github.com/yourusername/Security-Monitoring-Agent/discussions)

---

## Next Steps

After installation:
1. [User Guide](USER_GUIDE.md) - Learn how to use the system
2. [Authentication Setup](AUTHENTICATION.md) - Configure users and roles
3. [API Documentation](../api/API.md) - Integrate with other tools
