import requests
from twilio.rest import Client


api_key = "871cd962a374b54a25e39efd5d7c74a2"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
account_sid = 'AC3f0095f912fa35e4a058cbcb619fb534'
auth_token = '55874714bf680fcd96e52106f35f80f3'

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
        from_= '+16562187762',
        to= '+917300169695',
        body="It's going to rain today!!"
    )

    print(message.status)