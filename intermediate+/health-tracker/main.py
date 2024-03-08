from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv("../../.env")


GENDER = "Male"
WEIGHT_KG = 54
HEIGHT_CM = 168
AGE = 19

APP_ID = os.getenv("NUTRITIONIX_API_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_URL = "https://api.sheety.co/dac9fec623bca3a8b4ef73ce2d811c6c/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result["exercises"])

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_auth = (os.getenv("NUTRITIONIX_API_USERNAME"), os.getenv("NUTRITIONIX_API_PASSWORD"))

sheet_response = requests.post(sheety_URL, json=sheet_inputs, auth=sheety_auth)
print(sheet_response.text)