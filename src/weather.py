import os
import requests

class WeatherAPI:
    def __init__(self):
        # read API key from environment variable
        self.api_key = os.environ.get("WEATHER_API_KEY", "dummy_key_for_testing")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city):
        """will give you information about the weather in the given city"""
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",  # celsius
        }
        
        # it will not work if you have a dummy API key, so it will be mock now
        if self.api_key == "dummy_key_for_testing":
            return {
                "city": city,
                "temperature": 25.5,
                "description": "Partly cloudy",
                "humidity": 65,
                "status": "mock_data"
            }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                "city": data.get("name", city),
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "status": "success"
            }
        except Exception as e:
            return {"error": str(e), "status": "failed"}

# CLI interface
if __name__ == "__main__":
    api = WeatherAPI()
    city = input("Enter city name: ")
    result = api.get_weather(city)
    print(f"\nWeather in {result.get('city', city)}:")
    print(f"Temperature: {result.get('temperature', 'N/A')}°C")
    print(f"Description: {result.get('description', 'N/A')}")
    print(f"Humidity: {result.get('humidity', 'N/A')}%")
    print(f"Status: {result.get('status', 'unknown')}")
