# weather-repo
API testing
# Weather API Test Project 🌤️

[![Weather API Tests](https://github.com/MRDARKDEER/weather-repo/actions/workflows/test-api.yml/badge.svg)](https://github.com/MRDARKDEER/weather-repo/actions/workflows/test-api.yml)

## About
This project demonstrates GitHub Actions with API key management.

## Secrets Setup
1. Go to Settings → Secrets and variables → Actions
2. Add `WEATHER_API_KEY` as a repository secret
3. Use `dummy_key_for_testing` for testing

## Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests locally
pytest tests/ -v

# Run the app
python src/weather.py
