# Documentation Index

Welcome to the Security Monitoring Agent documentation!

## Quick Links

- [Setup Guide](SETUP_GUIDE.md) - Get started in 5 minutes
- [Project Structure](PROJECT_STRUCTURE.md) - Understand the codebase
- [API Documentation](API.md) - API reference and examples
- [ScaleDown Integration](SCALEDOWN_INTEGRATION.md) - How compression works
- [Anomaly Detection](ANOMALY_DETECTION.md) - Threat detection details

## What is this project?

A cybersecurity agent that:
1. **Compresses** security logs using ScaleDown API (30-70% token reduction)
2. **Detects** 8 types of security threats with AI-powered pattern matching
3. **Calculates** real-time cost savings in USD
4. **Displays** results in a beautiful interactive dashboard

## Features

✅ **ScaleDown Compression** - Reduce token usage and processing costs
✅ **8 Threat Types** - Brute Force, SQL Injection, Data Exfiltration, and more
✅ **Cost Dashboard** - See exactly how much money you save
✅ **Simple Interface** - Paste logs and click analyze
✅ **REST API** - Integrate with your existing tools

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key in .env file
echo "SCALEDOWN_API_KEY=your_key_here" > .env

# Run the server
python main.py

# Open browser
http://127.0.0.1:8001
```

## Architecture

```
User → Web UI → FastAPI Server → ScaleDown API → Threat Detection → Results
```

1. User submits security logs
2. Server compresses logs with ScaleDown
3. Detector analyzes for threats
4. Returns compression stats + threats + cost savings

## Tech Stack

- **Backend**: Python, FastAPI, Uvicorn
- **Compression**: ScaleDown REST API
- **Detection**: Regex patterns + AI analysis
- **Frontend**: HTML/CSS/JavaScript
- **Deployment**: Local (production-ready for cloud)

## Documentation Files

### [SETUP_GUIDE.md](SETUP_GUIDE.md)
Complete installation and configuration guide:
- Prerequisites
- Installation steps
- Environment setup
- Running the application
- Troubleshooting

### [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
Detailed project organization:
- Directory layout
- File descriptions
- Workflow explanation
- Technology decisions

### [API.md](API.md)
API reference documentation:
- Endpoint specifications
- Request/response formats
- Error handling
- Code examples

### [SCALEDOWN_INTEGRATION.md](SCALEDOWN_INTEGRATION.md)
ScaleDown compression details:
- How it works
- API integration
- Cost calculations
- Performance metrics

### [ANOMALY_DETECTION.md](ANOMALY_DETECTION.md)
Threat detection system:
- Pattern definitions
- Severity levels
- Confidence scoring
- Detection logic

## Project Status

✅ **Fully Operational**
- Server running on port 8001
- ScaleDown API integrated
- Threat detection working
- UI tested and functional
- Documentation complete

## Use Cases

1. **Security Analysis** - Analyze system logs for threats
2. **Cost Optimization** - Reduce LLM processing costs
3. **Automated Monitoring** - Integrate into security pipelines
4. **Threat Intelligence** - Compress and analyze threat data
5. **Compliance** - Efficient log retention and analysis

## Performance

- **Compression**: 30-70% token reduction
- **Speed**: 1-3 seconds for typical logs
- **Cost**: $0.15 per million tokens (GPT-4o-mini)
- **Accuracy**: 85-95% confidence on known patterns

## Next Steps

1. Read [SETUP_GUIDE.md](SETUP_GUIDE.md) to get started
2. Check [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) to understand the code
3. Try the sample logs from `logs/sample_logs.txt`
4. Explore the API at http://127.0.0.1:8001/docs

## Support

For questions or issues:
- Check the documentation
- Review code comments
- Test with sample logs
- Verify API key is set correctly

## License

MIT License - Feel free to use and modify

## Credits

Built with:
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [ScaleDown](https://scaledown.xyz/) - Compression API
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

---

**Start here:** [SETUP_GUIDE.md](SETUP_GUIDE.md)
