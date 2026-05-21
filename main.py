import requests
from dotenv import load_dotenv
import os
from pprint import pprint
from twillo import send_sms

load_dotenv()
API_KEY = os.getenv("API_KEY")

LAT = 18.51
LON = 73.85

endpoint = f"https://api.openweathermap.org/data/2.5/forecast"

wheather_params = {
    "lat": LAT,
    "lon": LON,
    "units": "metric",
    "cnt" : 4,
    "appid": API_KEY
}

print("Fetching DATA.....")
response = requests.get(url=endpoint, params=wheather_params, timeout=10)
response.raise_for_status()
response.encoding = 'utf-8'

data = response.json()
forcast = []
ids = []
print("DATA Fetched Successfully")
print(f"Response Status Code: {response.status_code}")

# pprint(data)
umbrella = False
# for key, value in data.items():
#     if key == "list":
#         for item in value:
#             forcast.append(item["weather"][0])
# pprint(forcast)

# for item in forcast:
#     if item["id"] < 700:
#         umbrella = True
#         break

for hourly_data in data["list"]:
    forcast.append(hourly_data["weather"][0])
    ids.append(hourly_data["weather"][0]["id"])
       
for id in ids:
    if id < 700:
        umbrella = True
        break

if umbrella:
    # print("Don't forget to take an umbrella today!")
    send_sms()

