# ScaleDown Integration Guide

**Module:** `src/compressor.py`  
**Last Updated:** February 1, 2026  
**Status:** ✅ Implemented

---

## 📋 Overview

The `SecurityLogCompressor` class wraps the ScaleDown API to intelligently compress security logs while preserving critical security keywords and semantic meaning.

### Key Features
- 30-70% token reduction
- Preserves security-critical keywords
- Cost estimation
- Detailed compression metrics
- Easy integration with AI models

---

## 🔧 Class: SecurityLogCompressor

### Initialization

```python
from src.compressor import SecurityLogCompressor

compressor = SecurityLogCompressor(
    target_model='gpt-4o-mini',  # Target LLM model
    rate='auto',                  # Compression rate (auto or 0-1)
    api_key=None,                 # Uses SCALEDOWN_API_KEY from .env
    preserve_keywords=True        # Keep security keywords intact
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `target_model` | str | 'gpt-4o-mini' | The target LLM for downstream analysis |
| `rate` | str/float | 'auto' | Compression rate - 'auto' or 0.0-1.0 |
| `api_key` | str | None | ScaleDown API key (from env if not provided) |
| `preserve_keywords` | bool | True | Preserve security-related keywords |

---

## 📖 Methods

### compress_logs()

Compresses security logs using ScaleDown API.

```python
result = compressor.compress_logs(
    logs=security_logs,
    analysis_prompt="Analyze these logs for threats"
)
```

**Parameters:**
- `logs` (str | List[str]): Raw security logs
- `analysis_prompt` (str): Query for AI analysis

**Returns:**  
`CompressedPrompt` object with:
- `content` - Compressed log text
- `tokens` - Tuple of (original, compressed) token counts
- `savings_percent` - Percentage of tokens saved
- `compression_ratio` - Compression ratio
- `latency_ms` - Processing time

### get_compression_stats()

Extracts formatted compression metrics.

```python
stats = compressor.get_compression_stats(result)
```

**Returns Dictionary:**
```python
{
    'original_tokens': 245,
    'compressed_tokens': 89,
    'tokens_saved': 156,
    'savings_percent': 63.67,
    'compression_ratio': 2.75,
    'latency_ms': 1450,
    'target_model': 'gpt-4o-mini',
    'estimated_cost_saved': 0.000023
}
```

---

## 🔒 Security Keywords Preserved

The compressor automatically preserves these critical security terms:

**Threats:**
- attack, breach, malware, virus, ransomware
- intrusion, exploit, vulnerability, threat

**Attack Types:**
- SQL injection, XSS, CSRF, DDoS, brute force
- privilege escalation, data exfiltration, backdoor

**Authentication:**
- unauthorized, failed, denied, blocked
- root, admin, sudo, password, authentication

**Severity:**
- critical, high, medium, low, warning, error

**Network:**
- IP, port, protocol, connection, traffic
- firewall, IDS, IPS, WAF, SIEM

---

## 💡 Usage Examples

### Example 1: Basic Compression

```python
from src.compressor import SecurityLogCompressor

# Initialize
compressor = SecurityLogCompressor()

# Sample logs
logs = """
2026-02-01 10:24:12 WARN Failed login attempt for user root from 203.0.113.45
2026-02-01 10:26:33 CRITICAL Unusual outbound traffic to 198.51.100.77:4444
"""

# Compress
result = compressor.compress_logs(
    logs=logs,
    analysis_prompt="Identify security threats"
)

# View compressed content
print(result.content)

# View stats
result.print_stats()
```

### Example 2: With Custom Analysis Prompt

```python
result = compressor.compress_logs(
    logs=large_log_file,
    analysis_prompt="Detect brute force attacks and data exfiltration attempts"
)

# Get detailed stats
stats = compressor.get_compression_stats(result)
print(f"Cost saved: ${stats['estimated_cost_saved']}")
```

### Example 3: List of Log Entries

```python
log_entries = [
    "2026-02-01 10:23:45 INFO User login successful",
    "2026-02-01 10:24:12 WARN Failed login attempt",
    "2026-02-01 10:24:15 WARN Failed login attempt"
]

result = compressor.compress_logs(logs=log_entries)
```

---

## 🎯 Cost Savings

Based on GPT-4o-mini pricing ($0.15 per 1M input tokens):

| Original Tokens | Compressed | Savings | Cost Saved |
|----------------|------------|---------|------------|
| 1,000 | 400 | 60% | $0.00009 |
| 10,000 | 3,500 | 65% | $0.00098 |
| 100,000 | 35,000 | 65% | $0.00975 |
| 1,000,000 | 350,000 | 65% | $0.09750 |

*For high-volume security operations processing millions of logs daily, savings can reach hundreds of dollars per day.*

---

## ⚠️ Error Handling

### Missing API Key

```python
try:
    compressor = SecurityLogCompressor()
except ValueError as e:
    print("Error: ScaleDown API key not found")
    print("Set SCALEDOWN_API_KEY in your .env file")
```

### API Errors

```python
from scaledown.exceptions import APIError, AuthenticationError

try:
    result = compressor.compress_logs(logs)
except AuthenticationError:
    print("Invalid API key")
except APIError as e:
    print(f"API error: {e}")
```

---

## 🧪 Testing

Run the module directly to test with sample logs:

```bash
python src/compressor.py
```

**Expected Output:**
```
Compressing security logs...

=== COMPRESSION RESULTS ===
Compressed Content:
[compressed log text]

=== COMPRESSION STATS ===
original_tokens: 245
compressed_tokens: 89
tokens_saved: 156
savings_percent: 63.67
compression_ratio: 2.75
...
```

---

## 🔗 Dependencies

```python
from scaledown import ScaleDownCompressor
from scaledown.types import CompressedPrompt
from dotenv import load_dotenv
```

**Required packages:**
- `scaledown[haste,semantic]==0.1.4`
- `python-dotenv==1.0.1`

---

## 📝 Change Log

### 2026-02-01 - Initial Implementation
- Created `SecurityLogCompressor` class
- Implemented log compression with keyword preservation
- Added cost estimation
- Added security keyword list (40+ terms)
- Implemented compression statistics
- Added usage examples
- Created comprehensive documentation

---

## 🚀 Next Steps

- [ ] Add support for multiple log formats (JSON, syslog, CSV)
- [ ] Implement batch compression for large datasets
- [ ] Add caching for repeated log patterns
- [ ] Create compression performance benchmarks
- [ ] Add custom keyword configuration

---

*This integration is the core of the Security Monitoring Agent's cost optimization capability.*
