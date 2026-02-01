# 🌐 Hosting Guide - Security Monitoring Agent

## ✅ Pre-Deployment Checklist

- [x] All code tested locally
- [x] Environment variables configured
- [x] Dependencies in requirements.txt
- [x] .env added to .gitignore
- [x] Code pushed to GitHub
- [x] Production-ready configuration

---

## 🚀 Hosting Options

### Option 1: Render (Recommended - Free Tier)

**Best for**: Easy deployment, free HTTPS, auto-deploy from GitHub

**Steps**:
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: security-monitoring-agent
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Instance Type**: Free

5. Add Environment Variables:
   ```
   SCALEDOWN_API_KEY = Mi5T2Bah347Zwm219z4g51u8kFCliV4k9qPiB39q
   SCALEDOWN_API_URL = https://api.scaledown.xyz/compress/raw/
   OPENAI_API_KEY = sk-proj-ric-YgWX... (optional)
   TARGET_MODEL = gpt-4o-mini
   HOST = 0.0.0.0
   PORT = 10000
   ```

6. Click "Deploy Web Service"
7. Wait 3-5 minutes for deployment
8. Access at: `https://security-monitoring-agent.onrender.com`

**Cost**: Free (with auto-sleep after 15 min inactivity)

---

### Option 2: Railway

**Best for**: Zero-config deployment, always-on free tier

**Steps**:
1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Python and deploys
5. Add environment variables in Settings → Variables:
   ```
   SCALEDOWN_API_KEY
   SCALEDOWN_API_URL
   OPENAI_API_KEY (optional)
   TARGET_MODEL
   ```
6. Railway automatically assigns a domain
7. Access at: `https://your-app.railway.app`

**Cost**: Free $5 credit/month (enough for this app)

---

### Option 3: PythonAnywhere

**Best for**: Simple Python hosting, beginner-friendly

**Steps**:
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Go to "Web" tab → "Add a new web app"
3. Choose "Manual configuration" → Python 3.10
4. Clone your repo:
   ```bash
   git clone https://github.com/Abin-Shaji-Thomas/Security-Monitoring-Agent.git
   cd Security-Monitoring-Agent
   ```
5. Create virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```
6. Configure WSGI file (use FastAPI with uvicorn)
7. Add environment variables in Web tab
8. Reload web app

**Cost**: Free tier available (limited CPU)

---

### Option 4: Heroku

**Best for**: Established platform, many add-ons

**Steps**:
1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create security-monitor-app`
4. Add Procfile:
   ```
   web: python main.py
   ```
5. Set environment variables:
   ```bash
   heroku config:set SCALEDOWN_API_KEY=your_key
   heroku config:set OPENAI_API_KEY=your_key
   ```
6. Deploy:
   ```bash
   git push heroku main
   ```
7. Open: `heroku open`

**Cost**: Free tier removed, starts at $7/month

---

### Option 5: AWS EC2 (Advanced)

**Best for**: Full control, scalability

**Steps**:
1. Launch EC2 instance (Ubuntu 22.04)
2. SSH into instance
3. Install dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```
4. Clone repository:
   ```bash
   git clone https://github.com/Abin-Shaji-Thomas/Security-Monitoring-Agent.git
   cd Security-Monitoring-Agent
   ```
5. Setup environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
6. Create .env file with your keys
7. Run with systemd service:
   ```bash
   sudo nano /etc/systemd/system/security-monitor.service
   ```
   ```ini
   [Unit]
   Description=Security Monitoring Agent
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/Security-Monitoring-Agent
   Environment="PATH=/home/ubuntu/Security-Monitoring-Agent/.venv/bin"
   ExecStart=/home/ubuntu/Security-Monitoring-Agent/.venv/bin/python main.py

   [Install]
   WantedBy=multi-user.target
   ```
8. Start service:
   ```bash
   sudo systemctl enable security-monitor
   sudo systemctl start security-monitor
   ```
9. Configure Nginx reverse proxy
10. Setup SSL with Let's Encrypt

**Cost**: ~$5-10/month (t2.micro)

---

### Option 6: DigitalOcean App Platform

**Best for**: Balance of simplicity and control

**Steps**:
1. Go to [digitalocean.com](https://www.digitalocean.com/products/app-platform)
2. Create new App
3. Connect GitHub repository
4. DigitalOcean auto-detects Python
5. Add environment variables
6. Deploy

**Cost**: $5/month basic tier

---

## 🔧 Production Configuration

### Update .env for Production

```env
# Production settings
HOST=0.0.0.0
PORT=8001  # Or use platform's PORT variable

# Required
SCALEDOWN_API_KEY=your_actual_key

# Optional
OPENAI_API_KEY=your_actual_key
TARGET_MODEL=gpt-4o-mini
```

### Security Considerations

1. **HTTPS**: Always use HTTPS in production (Render/Railway provide free SSL)
2. **API Keys**: Use platform's secret management, not .env in repo
3. **CORS**: Update allowed origins in production
4. **Rate Limiting**: Consider adding rate limiting for public APIs
5. **Authentication**: Add user authentication for production use

---

## 📊 Platform Comparison

| Platform | Free Tier | HTTPS | Auto-Deploy | Ease | Best For |
|----------|-----------|-------|-------------|------|----------|
| **Render** | ✅ Yes | ✅ Free | ✅ Yes | ⭐⭐⭐⭐⭐ | Beginners |
| **Railway** | ✅ $5 credit | ✅ Free | ✅ Yes | ⭐⭐⭐⭐⭐ | Quick deploy |
| **PythonAnywhere** | ✅ Limited | ✅ Paid | ❌ No | ⭐⭐⭐⭐ | Python focus |
| **Heroku** | ❌ No | ✅ Free | ✅ Yes | ⭐⭐⭐⭐ | Established |
| **AWS EC2** | ✅ 1yr trial | ⚙️ Manual | ❌ No | ⭐⭐ | Advanced users |
| **DigitalOcean** | ❌ No | ✅ Free | ✅ Yes | ⭐⭐⭐⭐ | Professional |

---

## 🎯 Recommended: Render (Free)

**Why Render**:
- ✅ Completely free tier
- ✅ Automatic HTTPS
- ✅ Deploy from GitHub in 2 minutes
- ✅ Auto-deploy on git push
- ✅ Easy environment variable management
- ✅ Health checks included
- ⚠️ Sleeps after 15 min inactivity (wakes in ~30 seconds)

**Quick Deploy to Render**:
```bash
# 1. Push to GitHub (already done)
git push

# 2. Go to render.com
# 3. Click "New" → "Web Service"
# 4. Connect GitHub repo
# 5. Use these settings:
#    - Build: pip install -r requirements.txt
#    - Start: python main.py
# 6. Add environment variables
# 7. Deploy!
```

Your app will be live at: `https://security-monitoring-agent-xxxx.onrender.com`

---

## 🧪 Test Deployment

After deploying, test:

1. **Homepage**: `https://your-app.com/` → Should show dashboard
2. **API Docs**: `https://your-app.com/docs` → Swagger UI
3. **Analyze Endpoint**: Test with sample data
4. **PDF Download**: Verify reports generate
5. **Health Check**: Ensure no errors in logs

---

## 🆘 Troubleshooting

### App won't start
- Check environment variables are set
- Verify requirements.txt is complete
- Check logs for import errors

### Port binding error
- Ensure PORT environment variable is set
- Use `0.0.0.0` for HOST, not `127.0.0.1`

### API key errors
- Verify keys are added to platform's environment variables
- Don't commit .env to GitHub
- Test keys locally first

### Memory issues
- Upgrade to paid tier if needed
- Optimize imports (lazy loading)
- Monitor resource usage

---

## 💰 Cost Estimates

**Free Options**:
- Render: Free (sleeps after inactivity)
- Railway: $5/month credit
- PythonAnywhere: Limited free tier

**Paid Options**:
- Render (always-on): $7/month
- Railway (unlimited): $10/month
- DigitalOcean: $5/month
- AWS EC2: $5-10/month
- Heroku: $7/month

---

## ✅ Final Checklist

Before going live:

- [ ] Test all features locally
- [ ] Update .env.example with correct variables
- [ ] Verify .env is in .gitignore
- [ ] Push latest code to GitHub
- [ ] Choose hosting platform
- [ ] Configure environment variables on platform
- [ ] Deploy and test
- [ ] Verify HTTPS is working
- [ ] Test all API endpoints
- [ ] Monitor logs for errors
- [ ] Set up uptime monitoring (optional)

---

## 🎉 You're Ready!

Your Security Monitoring Agent is production-ready and can be hosted on any of these platforms. **Render** is recommended for the easiest free deployment.

**Need help?** Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for more details.
