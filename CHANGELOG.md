# Changelog

All notable changes to Security Monitoring Agent will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-13

### 🚀 Major Features

#### Smart Compression System
- **Added** Natural language conversion for log compression
- **Added** ScaleDown API integration with gpt-4o model
- **Improved** Compression rates from 1-2% to 35-50%
- **Added** Verbose prose generation from structured logs
- **Added** Automatic pattern detection in log conversion

#### Authentication & Authorization
- **Added** JWT token-based authentication
- **Added** Role-Based Access Control (RBAC)
  - Admin role: Full system access
  - Analyst role: Analysis and export
  - Viewer role: Read-only access
- **Added** User management endpoints (CRUD operations)
- **Added** API key management per user
- **Changed** Password hashing from bcrypt to Argon2
- **Added** Default admin user (username: admin, password: admin123)

#### Multi-Format Export
- **Added** CSV export with clean formatting
- **Added** JSON export with complete metadata
- **Added** Excel export with multiple sheets:
  - Summary dashboard
  - Detailed threat list
  - IP intelligence data
  - Conditional formatting for critical threats
- **Added** Professional styling for Excel workbooks

#### User Interface Enhancements
- **Added** Dark mode toggle with localStorage persistence
- **Added** Interactive Chart.js visualizations:
  - Threat distribution (doughnut chart)
  - Cost savings (bar chart)
  - Security score (gauge chart)
- **Added** Drag & drop file upload zone
- **Added** File validation (10MB limit, supported formats)
- **Improved** Gradient backgrounds and animations
- **Added** CSS variable theming for light/dark modes
- **Improved** Responsive layout and mobile support

### 📊 Sample Datasets
- **Expanded** Sample 1 (Brute Force) from 10 to 40 lines
- **Expanded** Sample 2 (SQL Injection) from 9 to 36 lines
- **Expanded** Sample 3 (Ransomware) from 10 to 41 lines
- **Added** More context and detail to all sample datasets
- **Improved** Realism and variety in attack scenarios

### 🔧 Technical Improvements
- **Added** Virtual environment (.venv) for dependency isolation
- **Fixed** ScaleDown API model compatibility (gpt-4o instead of gpt-4o-mini)
- **Fixed** API response parsing for token counts
- **Improved** Error handling and logging
- **Added** Streaming response support
- **Added** HTTP Bearer authentication middleware

### 📚 Documentation
- **Added** Comprehensive README.md with features, installation, and usage
- **Added** CONTRIBUTING.md with development guidelines
- **Added** CHANGELOG.md (this file)
- **Added** API documentation structure
- **Added** Compression explanation guide

### 🐛 Bug Fixes
- **Fixed** bcrypt compatibility issues with Python 3.13
- **Fixed** Indentation error in require_role() function
- **Fixed** Username extraction in natural language converter
- **Fixed** Port conflict issues with server restart
- **Fixed** Compression ratio calculation and display

---

## [1.0.0] - 2025-12-01

### Initial Release

#### Core Features
- Basic log analysis with threat detection
- 13 threat pattern recognition:
  - Brute Force
  - SQL Injection
  - Ransomware
  - DDoS
  - Privilege Escalation
  - C2 Communication
  - Data Exfiltration
  - Malware
  - Phishing
  - And more...
- IP intelligence with geolocation
- Risk scoring system (CVSS-inspired)
- PDF report generation
- Basic web interface
- OpenAI API integration for insights
- Pattern learning with ML anomaly detection

#### Initial Components
- FastAPI backend
- SQLite databases for history
- Basic threat detection algorithms
- Simple HTML frontend
- ScaleDown API integration (initial)

---

## Upcoming Features (Roadmap)

### v2.1.0 (Planned)
- [ ] WebSocket support for real-time updates
- [ ] Email notifications for critical threats
- [ ] Advanced filtering and search
- [ ] Custom threat pattern definitions
- [ ] Multi-language support
- [ ] Scheduled analysis jobs

### v2.2.0 (Planned)
- [ ] Docker containerization
- [ ] Kubernetes deployment configs
- [ ] Redis caching layer
- [ ] Advanced ML models for anomaly detection
- [ ] Integration with SIEM systems
- [ ] Slack/Teams notifications

### v3.0.0 (Future)
- [ ] Distributed analysis cluster
- [ ] Real-time log streaming
- [ ] Advanced correlation engine
- [ ] Threat intelligence feed integration
- [ ] Custom dashboard builder
- [ ] Plugin system for extensions

---

## Support

For bug reports and feature requests, please use [GitHub Issues](https://github.com/yourusername/Security-Monitoring-Agent/issues).
