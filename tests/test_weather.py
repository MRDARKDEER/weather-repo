import sys
from pathlib import Path
from dotenv import load_dotenv

root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))


env_path = root_path / '.env'
load_dotenv(dotenv_path=env_path)

import os
print("API Key:",
os.getenv("WEATHER_API_KEY"))

import pytest
from src.weather import WeatherAPI

class TestWeatherAPI:
    def test_api_key_in_environment(self):
        """test: is there any API Key on your .env file?"""
        api_key = os.environ.get("WEATHER_API_KEY")
        # it would be your dummy or real API key
        assert api_key is not None, "WEATHER_API_KEY not set"

    def test_weather_api_mock_data(self):
        """test: checking for mock data by using dummy API key"""
        os.environ["WEATHER_API_KEY"] = "dummy_key_for_testing"
        api = WeatherAPI()
        result = api.get_weather("Dhaka")
        
        assert result["status"] == "mock_data"
        assert result["temperature"] == 25.5
        assert result["city"] == "Dhaka"

    def test_weather_api_with_real_key(self):
        """test: checking with real API key"""
        api_key = os.environ.get("WEATHER_API_KEY")
        
        # this test will will progress only if you have a real API key in your .env file
        if api_key and api_key != "dummy_key_for_testing":
            api = WeatherAPI()
            result = api.get_weather("London")
            assert result["status"] == "success"
            assert "temperature" in result
        else:
            # skip the test if no real API key is available
            pytest.skip("No real API key available for testing")

    def test_environment_variable_loaded(self):
        """test: check for loaded .env variables"""
        api = WeatherAPI()
        # API key should be real or dummy, but it should be loaded from the environment
        assert api.api_key is not None
