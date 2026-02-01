# API Documentation

## Base URL
http://127.0.0.1:8001

## POST /analyze

Main endpoint that compresses logs and detects threats.

**Request:**
```json
{
  "logs": "security log entries",
  "prompt": "Identify threats" (optional)
}
```

**Response:**
```json
{
  "success": true,
  "threats": [...],
  "compression_stats": {
    "original_tokens": 150,
    "compressed_tokens": 85,
    "tokens_saved": 65
  },
  "cost_savings": {
    "percentage_saved": 43.3,
    "estimated_cost_saved_usd": 0.00001,
    "latency_ms": 1234
  }
}
```

**Threat Object:**
- type: Threat category
- severity: CRITICAL/HIGH/MEDIUM/LOW
- description: What was detected
- recommendation: How to fix
- confidence: 0.0-1.0
- affected: List of IPs/users

## GET /health

Health check endpoint.

**Response:**
```json
{"status": "healthy", "version": "1.0.0"}
```

## GET /

Returns web interface HTML page.

## GET /docs

Interactive API documentation (Swagger UI).

## Code Examples

### Python
```python
import requests

response = requests.post(
    "http://127.0.0.1:8001/analyze",
    json={"logs": "your logs here", "prompt": "Find threats"}
)
result = response.json()
print(f"Threats: {len(result['threats'])}")
```

### cURL
```bash
curl -X POST http://127.0.0.1:8001/analyze \
  -H "Content-Type: application/json" \
  -d '{"logs": "test log", "prompt": "analyze"}'
```

### JavaScript
```javascript
const response = await fetch('http://127.0.0.1:8001/analyze', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({logs: 'logs here', prompt: 'Find threats'})
});
const data = await response.json();
```

## Error Responses

- **500** - Server error (compression or detection failed)
- **400** - Bad request (invalid input or missing API key)
