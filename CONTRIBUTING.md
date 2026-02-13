# Contributing to Security Monitoring Agent

First off, thank you for considering contributing to Security Monitoring Agent! It's people like you that make this project such a great tool for the security community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)

---

## Code of Conduct

This project and everyone participating in it is governed by respect, professionalism, and collaboration. By participating, you are expected to uphold this code.

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** and description
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment** (OS, Python version, dependencies)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Provide:

- **Clear use case** for the enhancement
- **Expected behavior** and benefits
- **Possible implementation** approach

### Pull Requests

- Fill in the required template
- Follow our coding standards
- Include tests for new features
- Update documentation as needed
- Link to related issues

---

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Security-Monitoring-Agent.git
cd Security-Monitoring-Agent

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/Security-Monitoring-Agent.git

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python test.py

# Start development server
python main.py
```

---

## Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, documented code
   - Add tests for new functionality
   - Update documentation

3. **Commit your changes**
   ```bash
   git commit -m "feat: add amazing feature"
   ```
   
   Use conventional commits:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `style:` Code style changes
   - `refactor:` Code refactoring
   - `test:` Test additions/changes
   - `chore:` Maintenance tasks

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Provide clear description
   - Link related issues
   - Add screenshots for UI changes
   - Ensure CI passes

---

## Coding Standards

### Python Style

- Follow **PEP 8** style guide
- Use **type hints** where applicable
- Maximum line length: **100 characters**
- Use **docstrings** for functions and classes

```python
def analyze_threat(log_entry: str, severity: int) -> Dict[str, Any]:
    """
    Analyze a log entry for security threats.
    
    Args:
        log_entry: The log text to analyze
        severity: Threat severity level (0-10)
    
    Returns:
        Dictionary containing threat analysis results
    """
    pass
```

### FastAPI Endpoints

```python
@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_logs(
    request: AnalysisRequest,
    current_user: User = Depends(get_current_user)
):
    """Analyze security logs with authentication."""
    pass
```

### Frontend Code

- Use **modern JavaScript** (ES6+)
- Keep functions **small and focused**
- Add **comments** for complex logic
- Follow **consistent naming** conventions

---

## Testing Guidelines

### Unit Tests

```python
def test_threat_detection():
    """Test threat detection accuracy."""
    logs = "Failed login attempt from 192.168.1.1"
    result = detect_threats(logs)
    assert result.severity == "HIGH"
    assert "Brute Force" in result.threat_type
```

### Integration Tests

Test complete workflows:
- Authentication flow
- Log analysis pipeline
- Export functionality
- API endpoints

### Test Coverage

- Aim for **80%+ code coverage**
- Test edge cases and error handling
- Mock external API calls

---

## Documentation

### Code Documentation

- Add docstrings to all public functions
- Include parameter types and return values
- Provide usage examples

### User Documentation

- Update README.md for new features
- Add guides to `docs/guides/`
- Include screenshots for UI changes
- Update API documentation

---

## Review Process

Pull requests require:
- ✅ Passing CI tests
- ✅ Code review approval
- ✅ Documentation updates
- ✅ No merge conflicts

Reviews focus on:
- Code quality and style
- Test coverage
- Security implications
- Performance impact
- Documentation completeness

---

## Questions?

Feel free to reach out:
- Open an issue for clarification
- Join discussions on GitHub
- Tag maintainers in PRs

---

Thank you for contributing! 🎉
