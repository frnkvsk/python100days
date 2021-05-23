import requests
import os


API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")
lat = 47.606209
lon = -122.332069
part = "current,minutely,daily,alerts"
ENDPOINT = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_KEY}"

response = requests.get(url=ENDPOINT)
response.raise_for_status()
data = response.json()
will_rain = False
weather_slice = data["hourly"][:48]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break
if will_rain:
    print("Bring an umbrella.")
