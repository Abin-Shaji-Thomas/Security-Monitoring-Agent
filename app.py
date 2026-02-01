"""
Security Monitoring Agent - Main Application
FastAPI backend for AI-powered security log analysis with ScaleDown compression
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import API routers
from api.compress import router as compress_router
from api.detect import router as detect_router
from api.analyze import router as analyze_router

# Create FastAPI app
app = FastAPI(
    title="Security Monitoring Agent",
    description="AI-powered threat detection with intelligent log compression using ScaleDown API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:8000,http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(compress_router)
app.include_router(detect_router)
app.include_router(analyze_router)

# Serve static files (frontend)
if os.path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main dashboard"""
    frontend_path = os.path.join("frontend", "index.html")
    
    if os.path.exists(frontend_path):
        return FileResponse(frontend_path)
    else:
        return """
        <html>
            <head>
                <title>Security Monitoring Agent</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        max-width: 800px;
                        margin: 50px auto;
                        padding: 20px;
                        background: #f5f5f5;
                    }
                    .container {
                        background: white;
                        padding: 40px;
                        border-radius: 10px;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                    }
                    h1 { color: #2c3e50; }
                    .status { color: #27ae60; font-weight: bold; }
                    a {
                        display: inline-block;
                        margin: 10px 10px 10px 0;
                        padding: 10px 20px;
                        background: #3498db;
                        color: white;
                        text-decoration: none;
                        border-radius: 5px;
                    }
                    a:hover { background: #2980b9; }
                    .version { color: #7f8c8d; font-size: 0.9em; }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🛡️ Security Monitoring Agent</h1>
                    <p class="status">✅ Backend is running!</p>
                    <p>AI-powered threat detection with intelligent log compression.</p>
                    
                    <h2>Quick Links:</h2>
                    <a href="/docs">📚 API Documentation</a>
                    <a href="/redoc">📖 ReDoc</a>
                    
                    <h2>Available Endpoints:</h2>
                    <ul>
                        <li><strong>POST /api/analyze</strong> - Complete log analysis (compression + detection)</li>
                        <li><strong>POST /api/compress</strong> - Compress logs with ScaleDown</li>
                        <li><strong>POST /api/detect</strong> - Detect anomalies in logs</li>
                        <li><strong>GET /health</strong> - Health check</li>
                    </ul>
                    
                    <p class="version">Version 0.1.0 | Powered by ScaleDown API</p>
                </div>
            </body>
        </html>
        """


@app.get("/health")
async def health():
    """Application health check"""
    return {
        "status": "healthy",
        "application": "Security Monitoring Agent",
        "version": "0.1.0",
        "services": {
            "compression": "available",
            "detection": "available",
            "analysis": "available"
        }
    }


@app.get("/api/info")
async def api_info():
    """Get API information and configuration"""
    return {
        "name": "Security Monitoring Agent API",
        "version": "0.1.0",
        "description": "AI-powered threat detection with ScaleDown compression",
        "endpoints": {
            "analyze": "/api/analyze - Complete analysis pipeline",
            "compress": "/api/compress - Log compression",
            "detect": "/api/detect - Anomaly detection"
        },
        "features": {
            "scaledown_compression": True,
            "pattern_based_detection": True,
            "ai_detection": "optional (requires OpenAI key)",
            "threat_patterns": 8
        },
        "documentation": {
            "swagger": "/docs",
            "redoc": "/redoc"
        }
    }


if __name__ == "__main__":
    import uvicorn
    
    # Get configuration from environment
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    print("=" * 60)
    print("🛡️  Security Monitoring Agent")
    print("=" * 60)
    print(f"📡 Server running at: http://{host}:{port}")
    print(f"📚 API Docs: http://{host}:{port}/docs")
    print(f"🔍 Health Check: http://{host}:{port}/health")
    print("=" * 60)
    
    uvicorn.run(
        "app:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info"
    )
