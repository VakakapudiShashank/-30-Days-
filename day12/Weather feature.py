import requests

def get_weather(city):
    try:
        api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()

        weather = {
            "City": data['name'],
            "Temperature (°C)": data['main']['temp'],
            "Weather": data['weather'][0]['description'].title(),
            "Humidity (%)": data['main']['humidity'],
            "Wind Speed (m/s)": data['wind']['speed']
        }
        return weather

    except requests.exceptions.HTTPError:
        return {"Error": "Invalid city name or API issue"}
    except requests.exceptions.RequestException:
        return {"Error": "Network error occurred"}
    except KeyError:
        return {"Error": "Unexpected response structure"}

# --------------------
# Main Program
# --------------------
if __name__ == "__main__":
    print("🌦 Weather Fetcher 🌦")
    city_name = input("Enter city name: ")
    result = get_weather(city_name)
    for key, value in result.items():
        print(f"{key}: {value}")
