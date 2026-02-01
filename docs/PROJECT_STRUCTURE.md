# Project Structure

**Last Updated:** February 1, 2026

---

## 📁 Directory Structure

```
Security-Monitoring-Agent/
├── api/                          # API endpoints and route handlers
│   ├── __init__.py              # ✅ API module initialization (v0.1.0)
│   ├── compress.py              # ✅ ScaleDown compression endpoint
│   ├── analyze.py               # ✅ Complete analysis endpoint
│   └── detect.py                # ✅ Anomaly detection endpoint
│
├── src/                          # Core application logic
│   ├── __init__.py              # ✅ Core module initialization (v0.1.0)
│   ├── compressor.py            # ✅ ScaleDown API wrapper
│   ├── analyzer.py              # [TODO] AI model integration
│   ├── detector.py              # ✅ Anomaly detection algorithms
│   └── utils.py                 # ✅ Helper functions
│
├── frontend/                     # Web dashboard UI
│   ├── index.html               # [TODO] Main dashboard page
│   ├── styles.css               # [TODO] Dashboard styling
│   └── script.js                # [TODO] Frontend logic
│
├── logs/                         # Sample log files for testing
│   └── sample_logs.txt          # ✅ Demo security logs (37 entries)
│
├── tests/                        # Unit and integration tests
│   ├── test_compression.py      # [TODO] Compression tests
│   ├── test_analysis.py         # [TODO] Analysis tests
│   └── test_detection.py        # [TODO] Detection tests
│
├── docs/                         # Project documentation
│   ├── INDEX.md                 # ✅ Documentation index
│   ├── PROJECT_STRUCTURE.md     # ✅ This file
│   ├── API.md                   # ✅ API endpoint documentation
│   ├── ARCHITECTURE.md          # [TODO] System architecture
│   ├── DEVELOPMENT_LOG.md       # ✅ Development changelog
│   ├── SETUP_GUIDE.md           # [TODO] Setup instructions
│   ├── USAGE_GUIDE.md           # [TODO] Usage guide
│   ├── SCALEDOWN_INTEGRATION.md # ✅ ScaleDown integration docs
│   └── ANOMALY_DETECTION.md     # ✅ Detection documentation
│
├── .env.example                  # ✅ Environment variables template
├── .gitignore                    # ✅ Git ignore rules
├── requirements.txt              # ✅ Python dependencies
├── README.md                     # ✅ project README
├── app.py                        # [TODO] Main FastAPI application
└── vercel.json                   # [TODO] Vercel deployment config
```

---

## 📦 Module Descriptions

### `/api` - API Layer
Contains FastAPI route handlers and endpoint definitions.

**Files:** ✅
- `compress.py` - Handles log compression requests via ScaleDown API ✅
- `analyze.py` - Complete analysis pipeline (compression + detection) ✅
- `detect.py` - Manages anomaly detection operations ✅
- `detect.py` - Manages anomaly detection operations

### `/src` - Core Logic Layer
Contains business logic and service implementations.

**Files:**
- `__init__.py` - Module initialization ✅
- `compressor.py` - ScaleDown API integration wrapper ✅
- `analyzer.py` - AI model service for threat analysis [TODO]
- `detector.py` - Anomaly detection algorithms (pattern + AI-based) ✅
- `utils.py` - Shared utility functions (log parsing, formatting, IP extraction) ✅

### `/frontend` - Presentation Layer
Simple web interface for user interactions.

**Files:**
- `index.html` - Main dashboard HTML
- `styles.css` - CSS styling
- `script.js` - Client-side JavaScript logic

### `/logs` - Sample Data
Demo and test log files.

### `/tests` - Testing Layer
Unit tests and integration tests.

### `/docs` - Documentation
Comprehensive project documentation (this folder).

---

## 🔄 Status Legend

- ✅ **Complete** - File exists and implemented
- [TODO] - File planned but not yet created
- 🔄 **In Progress** - Currently being developed
- ⚠️ **Deprecated** - Marked for removal

---

## 📝 Change Log

### 2026-02-01
- Created folder structure
- Added `__init__.py` files to api/ and src/
- Initialized documentation system
- ✅ Implemented `src/compressor.py` - ScaleDown compression integration
- ✅ Implemented `src/detector.py` - Anomaly detection with 8 threat 
- ✅ Implemented `api/compress.py` - Compression API endpoint
- ✅ Implemented `api/detect.py` - Detection API endpoint
- ✅ Implemented `api/analyze.py` - Complete analysis endpoint
- ✅ Created `app.py` - Main FastAPI application
- ✅ Added sample security logs (37 entries with various threats)
- ✅ Created API documentationpatterns
- ✅ Implemented `src/utils.py` - Helper functions for log processing

---

*This document is automatically updated when the project structure changes.*
