@echo off
cls
echo ========================================
echo Security Monitoring Agent v2.0
echo Quick Setup Script
echo ========================================
echo.

REM Check if .env exists
if exist .env (
    echo [OK] .env file already configured with API keys
) else (
    echo [!] Creating .env file from template...
    copy .env.example .env
    echo.
    echo [ACTION NEEDED] Please edit .env file and add your API keys:
    echo   - SCALEDOWN_API_KEY  (REQUIRED - get from https://scaledown.xyz)
    echo   - OPENAI_API_KEY     (OPTIONAL - get from https://platform.openai.com/api-keys)
    echo.
    pause
    notepad .env
)

echo.
echo [1/4] Checking Python installation...
python --version
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python 3.8+
    pause
    exit /b 1
)

echo.
echo [2/4] Setting up virtual environment...
if not exist .venv (
    python -m venv .venv
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment already exists
)

echo.
echo [3/4] Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo [4/4] Installing dependencies (this may take a few minutes)...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the server, run:
echo   python main.py
echo.
echo Then open your browser to:
echo   http://127.0.0.1:8001
echo.
echo Default login:
echo   Username: admin
echo   Password: admin123
echo.
echo See DEMO_SETUP.md for complete demo guide!
echo.
pause
