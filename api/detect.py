"""
Detection API Endpoint
Handles anomaly detection in security logs
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.detector import SecurityLogDetector, Anomaly, ThreatLevel

router = APIRouter(prefix="/api/detect", tags=["detection"])


class DetectionRequest(BaseModel):
    """Request model for anomaly detection"""
    logs: str = Field(..., description="Security logs to analyze", min_length=1)
    compressed_context: Optional[str] = Field(
        default=None,
        description="Compressed logs from ScaleDown (for AI analysis)"
    )
    ai_enabled: bool = Field(
        default=False,
        description="Enable AI-powered detection"
    )


class AnomalyModel(BaseModel):
    """Model for detected anomaly"""
    type: str
    severity: str
    description: str
    recommendation: str
    confidence: float
    affected_resources: List[str]


class DetectionResponse(BaseModel):
    """Response model for detection results"""
    success: bool
    anomalies: List[AnomalyModel]
    anomaly_count: int
    overall_threat_level: str
    threat_summary: Dict[str, int]
    error: Optional[str] = None


@router.post("/", response_model=DetectionResponse)
async def detect_anomalies(request: DetectionRequest):
    """
    Detect security anomalies in logs
    
    - **logs**: Raw security log text to analyze
    - **compressed_context**: Compressed logs for AI analysis (optional)
    - **ai_enabled**: Enable AI-powered detection (requires OpenAI key)
    
    Returns list of detected anomalies with severity levels
    """
    try:
        # Initialize detector
        detector = SecurityLogDetector(ai_enabled=request.ai_enabled)
        
        # Detect anomalies
        anomalies = detector.detect_anomalies(
            logs=request.logs,
            compressed_context=request.compressed_context
        )
        
        # Calculate overall threat level
        overall_threat = detector.calculate_threat_level(anomalies)
        
        # Create threat summary by severity
        threat_summary = _create_threat_summary(anomalies)
        
        # Convert anomalies to response models
        anomaly_models = [
            AnomalyModel(
                type=a.type.value,
                severity=a.severity.value,
                description=a.description,
                recommendation=a.recommendation,
                confidence=a.confidence,
                affected_resources=a.affected_resources
            )
            for a in anomalies
        ]
        
        return DetectionResponse(
            success=True,
            anomalies=anomaly_models,
            anomaly_count=len(anomalies),
            overall_threat_level=overall_threat.value,
            threat_summary=threat_summary,
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
            detail=f"Detection failed: {str(e)}"
        )


def _create_threat_summary(anomalies: List[Anomaly]) -> Dict[str, int]:
    """Create summary of threats by severity"""
    summary = {
        "CRITICAL": 0,
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
        "INFO": 0
    }
    
    for anomaly in anomalies:
        summary[anomaly.severity.value] += 1
    
    return summary


@router.get("/health")
async def health_check():
    """Health check endpoint for detection service"""
    return {
        "status": "healthy",
        "service": "detection",
        "version": "0.1.0",
        "patterns_loaded": 8
    }
