# ScaleDown Integration

## How It Works

1. User submits security logs via web interface
2. `compressor.py` sends HTTP POST to ScaleDown API
3. ScaleDown compresses the context intelligently
4. Returns compressed text with token usage metrics
5. We calculate cost savings based on token reduction

## Implementation Details

Using **REST API** (not Python package) for direct control:

```python
import requests

headers = {
    'x-api-key': api_key,
    'Content-Type': 'application/json'
}

payload = {
    'context': logs,
    'prompt': analysis_prompt,
    'model': 'gpt-4o-mini',
    'max_tokens': 500,
    'scaledown': {'rate': 'auto'}
}

response = requests.post(
    'https://api.scaledown.xyz/compress/raw/',
    headers=headers,
    json=payload,
    timeout=30
)
```

## Metrics Calculated

| Metric | Description | Formula |
|--------|-------------|---------|
| **Original Tokens** | Tokens in raw logs | `len(logs.split())` |
| **Compressed Tokens** | Tokens after compression | From API response |
| **Tokens Saved** | Reduction amount | `original - compressed` |
| **Percentage Saved** | Compression ratio % | `(saved / original) * 100` |
| **Compression Ratio** | Size ratio | `original / compressed` |
| **Cost Saved (USD)** | Money saved | `(saved / 1M) * $0.15` |

## Performance

- **Typical Compression**: 30-70% token reduction
- **API Latency**: 1-3 seconds for most logs
- **Timeout**: 30 seconds max
- **Rate**: Auto-optimized by ScaleDown

## Cost Calculation

Based on **GPT-4o-mini pricing**: $0.15 per 1M input tokens

### Example:
- Original: 100,000 tokens
- Compressed: 40,000 tokens
- Saved: 60,000 tokens
- **Cost saved**: $0.009 USD per request

### At Scale:
- 1,000 requests/day
- 60,000 tokens saved each
- **Annual savings**: $3,285 USD

## API Response Structure

```json
{
  "choices": [{
    "message": {
      "content": "AI analysis..."
    }
  }],
  "compressed_context": "Compressed logs...",
  "usage": {
    "prompt_tokens": 85,
    "prompt_tokens_uncompressed": 150
  }
}
```

## Why REST API Instead of Package?

1. **Direct Control** - Full control over requests
2. **Simple Dependencies** - Just `requests` library
3. **Easier Debugging** - See exact HTTP calls
4. **No Version Conflicts** - No heavy package dependencies
5. **Proven Working** - Based on your test.py example

## Configuration

In `.env` file:
```
SCALEDOWN_API_KEY=your_api_key_here
SCALEDOWN_API_URL=https://api.scaledown.xyz/compress/raw/
TARGET_MODEL=gpt-4o-mini
```

Simple and effective!
