"""
Simple Security Monitoring Agent - Main Application
Compresses logs with ScaleDown → Detects threats → Shows cost savings
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from typing import List, Dict, Any
import os

from src.compressor import SecurityLogCompressor
from src.detector import SecurityLogDetector

app = FastAPI(
    title="Security Monitoring Agent",
    description="Compress security logs and detect threats with cost savings",
    version="1.0.0"
)

# Request/Response Models
class AnalyzeRequest(BaseModel):
    logs: str
    prompt: str = "Identify security threats and anomalies"

class ThreatInfo(BaseModel):
    type: str
    severity: str
    description: str
    recommendation: str
    confidence: float
    affected: List[str]

class AnalyzeResponse(BaseModel):
    success: bool
    compressed_context: str
    ai_response: str
    threats: List[ThreatInfo]
    compression_stats: Dict[str, Any]
    cost_savings: Dict[str, Any]


@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    """Serve the main HTML page"""
    html_file = "frontend/index.html"
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            return HTMLResponse(content=f.read())
    else:
        return HTMLResponse(content="""
        <html><body><h1>Security Monitoring Agent</h1>
        <p>Frontend not found. API available at <a href="/docs">/docs</a></p>
        </body></html>
        """)


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_security_logs(request: AnalyzeRequest):
    """
    Main endpoint: Compress logs → Detect threats → Return results with cost savings
    """
    try:
        # Step 1: Compress logs with ScaleDown
        compressor = SecurityLogCompressor()
        compression_result = compressor.compress_logs(
            logs=request.logs,
            prompt=request.prompt
        )
        
        # Step 2: Detect anomalies
        detector = SecurityLogDetector()
        anomalies = detector.detect_anomalies(
            logs=request.logs,
            compressed_context=compression_result.get('compressed_context')
        )
        
        # Step 3: Calculate compression stats
        stats = compressor.get_compression_stats(compression_result)
        
        # Step 4: Calculate cost savings
        cost_savings = {
            'tokens_saved': stats['tokens_saved'],
            'percentage_saved': stats['savings_percent'],
            'compression_ratio': stats['compression_ratio'],
            'estimated_cost_saved_usd': stats['estimated_cost_saved'],
            'latency_ms': stats['latency_ms']
        }
        
        # Step 5: Format threats
        threats = []
        for anomaly in anomalies:
            threats.append(ThreatInfo(
                type=anomaly.type.value,
                severity=anomaly.severity.value,
                description=anomaly.description,
                recommendation=anomaly.recommendation,
                confidence=anomaly.confidence,
                affected=anomaly.affected_resources[:5]  # Limit to 5
            ))
        
        return AnalyzeResponse(
            success=True,
            compressed_context=compression_result.get('compressed_context', ''),
            ai_response=compression_result.get('content', 'Analysis complete'),
            threats=threats,
            compression_stats={
                'original_tokens': stats['original_tokens'],
                'compressed_tokens': stats['compressed_tokens'],
                'tokens_saved': stats['tokens_saved']
            },
            cost_savings=cost_savings
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Security Monitoring Agent",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
