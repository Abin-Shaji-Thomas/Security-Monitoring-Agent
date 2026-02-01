# API Documentation

**Last Updated:** February 1, 2026  
**Version:** 0.1.0

---

## 📡 Base URL

```
Local: http://localhost:8000
Production: https://your-deployment.vercel.app
```

---

## 🔑 Authentication

Currently, the API is open for development. In production, you'll need to configure API keys in the `.env` file.

Required environment variables:
- `SCALEDOWN_API_KEY` - Your ScaleDown API key
- `OPENAI_API_KEY` - Your OpenAI API key (optional, for AI detection)

---

## 📚 Endpoints

### 1. Complete Analysis (Recommended)

**POST** `/api/analyze`

Complete security log analysis pipeline combining compression and detection.

**Request Body:**
```json
{
  "logs": "2026-02-01 10:24:12 WARN Failed login attempt...",
  "enable_compression": true,
  "enable_ai_detection": false,
  "target_model": "gpt-4o-mini"
}
```

**Parameters:**
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| logs | string | ✅ Yes | - | Raw security logs to analyze |
| enable_compression | boolean | No | true | Use ScaleDown compression |
| enable_ai_detection | boolean | No | false | Enable AI-powered detection |
| target_model | string | No | gpt-4o-mini | Target AI model |

**Response:**
```json
{
  "success": true,
  "compression": {
    "original_tokens": 245,
    "compressed_tokens": 89,
    "tokens_saved": 156,
    "savings_percent": 63.67,
    "compression_ratio": 2.75,
    "latency_ms": 1450,
    "target_model": "gpt-4o-mini",
    "estimated_cost_saved": 0.000023
  },
  "detection": {
    "anomalies": [
      {
        "type": "Brute Force Attack",
        "severity": "HIGH",
        "description": "Multiple failed login attempts detected (4 occurrences)",
        "recommendation": "Immediately block source IP...",
        "confidence": "85%",
        "affected": ["root", "203.0.113.45"]
      }
    ],
    "anomaly_count": 2,
    "overall_threat_level": "CRITICAL"
  },
  "summary": {
    "total_anomalies": 2,
    "threat_level": "CRITICAL",
    "compression_enabled": true,
    "ai_detection_enabled": false,
    "tokens_saved": 156,
    "savings_percent": "63.7%",
    "cost_saved": "$0.000023"
  }
}
```

---

### 2. Compress Logs

**POST** `/api/compress`

Compress security logs using ScaleDown API.

**Request Body:**
```json
{
  "logs": "Your security logs here...",
  "prompt": "Analyze these logs for threats",
  "target_model": "gpt-4o-mini",
  "rate": "auto"
}
```

**Parameters:**
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| logs | string | ✅ Yes | - | Security logs to compress |
| prompt | string | No | "Analyze these security logs..." | Analysis prompt |
| target_model | string | No | gpt-4o-mini | Target AI model |
| rate | string | No | auto | Compression rate |

**Response:**
```json
{
  "success": true,
  "compressed_content": "Compressed log text...",
  "stats": {
    "original_tokens": 245,
    "compressed_tokens": 89,
    "tokens_saved": 156,
    "savings_percent": 63.67,
    "compression_ratio": 2.75,
    "latency_ms": 1450,
    "target_model": "gpt-4o-mini",
    "estimated_cost_saved": 0.000023
  }
}
```

---

### 3. Detect Anomalies

**POST** `/api/detect`

Detect security anomalies and threats in logs.

**Request Body:**
```json
{
  "logs": "Your security logs here...",
  "compressed_context": null,
  "ai_enabled": false
}
```

**Parameters:**
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| logs | string | ✅ Yes | - | Security logs to analyze |
| compressed_context | string | No | null | Compressed logs for AI analysis |
| ai_enabled | boolean | No | false | Enable AI detection |

**Response:**
```json
{
  "success": true,
  "anomalies": [
    {
      "type": "Brute Force Attack",
      "severity": "HIGH",
      "description": "Multiple failed login attempts detected (3 occurrences)",
      "recommendation": "Immediately block source IP...",
      "confidence": 0.85,
      "affected_resources": ["root", "203.0.113.45"]
    }
  ],
  "anomaly_count": 1,
  "overall_threat_level": "HIGH",
  "threat_summary": {
    "CRITICAL": 0,
    "HIGH": 1,
    "MEDIUM": 0,
    "LOW": 0,
    "INFO": 0
  }
}
```

---

### 4. Health Check

**GET** `/health`

Check if the application is running.

**Response:**
```json
{
  "status": "healthy",
  "application": "Security Monitoring Agent",
  "version": "0.1.0",
  "services": {
    "compression": "available",
    "detection": "available",
    "analysis": "available"
  }
}
```

---

### 5. API Info

**GET** `/api/info`

Get information about the API.

**Response:**
```json
{
  "name": "Security Monitoring Agent API",
  "version": "0.1.0",
  "description": "AI-powered threat detection with ScaleDown compression",
  "endpoints": {...},
  "features": {...},
  "documentation": {...}
}
```

---

## 🧪 Example Usage

### Using cURL

```bash
# Complete analysis
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "logs": "2026-02-01 10:24:12 WARN Failed login attempt for user root from 203.0.113.45",
    "enable_compression": true,
    "enable_ai_detection": false
  }'
```

### Using Python

```python
import requests

# Analyze logs
response = requests.post(
    "http://localhost:8000/api/analyze",
    json={
        "logs": """
        2026-02-01 10:24:12 WARN Failed login attempt
        2026-02-01 10:26:33 CRITICAL Suspicious traffic detected
        """,
        "enable_compression": True,
        "enable_ai_detection": False
    }
)

result = response.json()
print(f"Threat Level: {result['summary']['threat_level']}")
print(f"Anomalies: {result['detection']['anomaly_count']}")
print(f"Tokens Saved: {result['summary']['tokens_saved']}")
```

### Using JavaScript (Fetch)

```javascript
const response = await fetch('http://localhost:8000/api/analyze', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    logs: "2026-02-01 10:24:12 WARN Failed login attempt...",
    enable_compression: true,
    enable_ai_detection: false
  })
});

const result = await response.json();
console.log('Threat Level:', result.summary.threat_level);
```

---

## ❌ Error Responses

### 400 Bad Request
```json
{
  "detail": "Configuration error: ScaleDown API key not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Analysis failed: Connection timeout"
}
```

---

## 📊 Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid parameters |
| 500 | Server Error - Processing failed |

---

## 🚀 Interactive Documentation

Visit the following URLs for interactive API documentation:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 💡 Best Practices

1. **Always enable compression** to reduce costs (30-70% savings)
2. **Use pattern-based detection** first (faster, no extra costs)
3. **Enable AI detection** only for complex analysis requiring deep insights
4. **Batch logs** when possible for better compression ratios
5. **Monitor your API usage** to stay within limits

---

## 🔒 Security Notes

- Never expose your API keys in client-side code
- Use environment variables for all sensitive configuration
- Implement rate limiting in production
- Add authentication for public deployments
- Validate and sanitize all log inputs

---

*For more details, see the [main README](../README.md) and [interactive docs](http://localhost:8000/docs).*
