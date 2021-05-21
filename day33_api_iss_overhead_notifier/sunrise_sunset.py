import requests

MY_LATITUDE = 47.606209
MY_LONGITUDE = -122.332069
data = {
    "lng": MY_LONGITUDE,
    "lat": MY_LATITUDE,
    "formatted": 1
}
response = requests.get("https://api.sunrise-sunset.org/json", params=data)
response.raise_for_status()
response_data = response.json()

for key in response_data["results"]:
    print(key, response_data['results'][key])