# Project Structure

Clean, organized codebase with 3 core modules and 1 web interface.

## Directory Layout

\Security-Monitoring-Agent/
 src/                   # Core modules
    compressor.py     # ScaleDown API (42 lines)
    detector.py       # Threat detection (413 lines)
    utils.py          # Helpers (100+ lines)
 frontend/             # Web UI
    index.html       # Dashboard (350 lines)
 docs/                 # Documentation
 logs/                 # Sample data
    sample_logs.txt
 main.py              # Entry point (133 lines)
 test.py              # ScaleDown example
 requirements.txt     # Dependencies
 .env                 # API keys
\
## File Descriptions

### main.py (Entry Point)
FastAPI application with single /analyze endpoint.
- Orchestrates compression + detection workflow
- Serves frontend HTML
- Handles errors and validation

### src/compressor.py
ScaleDown REST API integration using requests library.
- compress_logs() - Calls ScaleDown API
- get_compression_stats() - Calculates metrics
- Simple, no complex dependencies

### src/detector.py  
Pattern-based threat detection with 8 threat types.
- detect_anomalies() - Main detection function
- 8 regex patterns for common threats
- Confidence scoring and deduplication

### frontend/index.html
Beautiful single-page dashboard.
- Gradient design with purple theme
- Real-time cost savings display
- Interactive threat cards with color coding
- Sample log loader button

## Workflow

1. User  Browser  http://127.0.0.1:8001
2. User clicks Analyze
3. Frontend  POST /analyze  main.py
4. main.py  compressor.py  ScaleDown API
5. main.py  detector.py  Pattern matching
6. main.py  Response with stats + threats
7. Frontend  Display results

Simple linear flow, no complexity.

## Technology Choices

**FastAPI** - Modern, fast, automatic API docs
**Requests** - Simple HTTP client for ScaleDown
**Pure HTML/CSS/JS** - No build tools needed
**Virtual Environment** - Isolated dependencies
**File-based logs** - No database required

## What We Removed

- Old app.py (replaced by main.py)
- api/ folder (unnecessary structure)
- Test files (not needed in production)
- ScaleDown Python package (using REST API instead)

Clean = Maintainable
