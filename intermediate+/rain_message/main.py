import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv('../.env')

api_key = os.getenv('API_KEY')
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

parametres = {
    "lat": 27.476219,
    "lon": 77.693398,
    "appid" : api_key,
    "cnt": 4
}

response = requests.get(OWN_ENDPOINT,parametres)
response.raise_for_status()
data = response.json()
# print(data["weather"][0]["id"])
will_rain = False
for now_data in data:
    condition = now_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        from_= os.getenv("TWILIO_NUM"),
        to= os.getenv("MY_NUM"),
        body="It's going to rain today!!"
    )

    print(message.status)