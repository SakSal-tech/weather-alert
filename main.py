import requests

url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "8c38584889ca36d0bca30f35cdd15d4b"
my_lat = 51.5072
my_lon = -0.1276
parameters = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(
    url, params=parameters
)
response.raise_for_status()
weather_data = response.json()
will_rain = False
#print(weather_data["weather"][0])
for hour_data in weather_data["weather"]:
    condition_code = (hour_data["id"])
    #print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
