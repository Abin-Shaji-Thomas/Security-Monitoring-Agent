"""
Compression API Endpoint
Handles security log compression using ScaleDown API
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.compressor import SecurityLogCompressor

router = APIRouter(prefix="/api/compress", tags=["compression"])


class CompressionRequest(BaseModel):
    """Request model for log compression"""
    logs: str = Field(..., description="Security logs to compress", min_length=1)
    prompt: str = Field(
        default="Analyze these security logs for threats and anomalies",
        description="Analysis prompt/query"
    )
    target_model: Optional[str] = Field(
        default=None,
        description="Target AI model (default: gpt-4o-mini)"
    )
    rate: Optional[str] = Field(
        default="auto",
        description="Compression rate ('auto' or 0.0-1.0)"
    )


class CompressionResponse(BaseModel):
    """Response model for compression results"""
    success: bool
    compressed_content: str
    stats: Dict[str, Any]
    error: Optional[str] = None


@router.post("/", response_model=CompressionResponse)
async def compress_logs(request: CompressionRequest):
    """
    Compress security logs using ScaleDown API
    
    - **logs**: Raw security log text to compress
    - **prompt**: Analysis query for AI (optional)
    - **target_model**: Target LLM model (optional)
    - **rate**: Compression rate (optional, default: auto)
    
    Returns compressed logs with compression statistics
    """
    try:
        # Initialize compressor
        compressor = SecurityLogCompressor(
            target_model=request.target_model,
            rate=request.rate
        )
        
        # Compress logs
        result = compressor.compress_logs(
            logs=request.logs,
            analysis_prompt=request.prompt
        )
        
        # Get detailed stats
        stats = compressor.get_compression_stats(result)
        
        return CompressionResponse(
            success=True,
            compressed_content=result.content,
            stats=stats,
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
            detail=f"Compression failed: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """Health check endpoint for compression service"""
    return {
        "status": "healthy",
        "service": "compression",
        "version": "0.1.0"
    }
