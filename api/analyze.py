"""
Analysis API Endpoint
Combines compression and detection for complete log analysis
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.compressor import SecurityLogCompressor
from src.detector import SecurityLogDetector

router = APIRouter(prefix="/api/analyze", tags=["analysis"])


class AnalysisRequest(BaseModel):
    """Request model for complete log analysis"""
    logs: str = Field(..., description="Security logs to analyze", min_length=1)
    enable_compression: bool = Field(
        default=True,
        description="Use ScaleDown compression"
    )
    enable_ai_detection: bool = Field(
        default=False,
        description="Enable AI-powered threat detection"
    )
    target_model: Optional[str] = Field(
        default=None,
        description="Target AI model"
    )


class AnalysisResponse(BaseModel):
    """Response model for complete analysis"""
    success: bool
    compression: Optional[Dict[str, Any]] = None
    detection: Dict[str, Any]
    summary: Dict[str, Any]
    error: Optional[str] = None


@router.post("/", response_model=AnalysisResponse)
async def analyze_logs(request: AnalysisRequest):
    """
    Complete security log analysis pipeline
    
    Combines ScaleDown compression and anomaly detection in one call.
    
    - **logs**: Raw security log text to analyze
    - **enable_compression**: Use ScaleDown compression (saves costs)
    - **enable_ai_detection**: Enable AI-powered detection
    - **target_model**: Target AI model (optional)
    
    Returns compression stats, detected anomalies, and overall assessment
    """
    try:
        compressed_content = None
        compression_stats = None
        
        # Step 1: Compress logs (if enabled)
        if request.enable_compression:
            compressor = SecurityLogCompressor(target_model=request.target_model)
            compression_result = compressor.compress_logs(
                logs=request.logs,
                analysis_prompt="Analyze for security threats and anomalies"
            )
            compressed_content = compression_result.content
            compression_stats = compressor.get_compression_stats(compression_result)
        
        # Step 2: Detect anomalies
        detector = SecurityLogDetector(ai_enabled=request.enable_ai_detection)
        anomalies = detector.detect_anomalies(
            logs=request.logs,
            compressed_context=compressed_content
        )
        
        # Step 3: Calculate overall threat
        overall_threat = detector.calculate_threat_level(anomalies)
        
        # Build response
        detection_results = {
            "anomalies": [
                {
                    "type": a.type.value,
                    "severity": a.severity.value,
                    "description": a.description,
                    "recommendation": a.recommendation,
                    "confidence": f"{a.confidence:.0%}",
                    "affected": a.affected_resources[:3]
                }
                for a in anomalies
            ],
            "anomaly_count": len(anomalies),
            "overall_threat_level": overall_threat.value
        }
        
        # Create summary
        summary = {
            "total_anomalies": len(anomalies),
            "threat_level": overall_threat.value,
            "compression_enabled": request.enable_compression,
            "ai_detection_enabled": request.enable_ai_detection
        }
        
        if compression_stats:
            summary["tokens_saved"] = compression_stats.get("tokens_saved", 0)
            summary["savings_percent"] = f"{compression_stats.get('savings_percent', 0):.1f}%"
            summary["cost_saved"] = f"${compression_stats.get('estimated_cost_saved', 0):.6f}"
        
        return AnalysisResponse(
            success=True,
            compression=compression_stats if request.enable_compression else None,
            detection=detection_results,
            summary=summary,
            error=None
        )
        
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Configuration error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """Health check endpoint for analysis service"""
    return {
        "status": "healthy",
        "service": "analysis",
        "version": "0.1.0"
    }
