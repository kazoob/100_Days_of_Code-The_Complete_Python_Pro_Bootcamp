import os
import requests
from datetime import datetime

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": os.environ["NUTRITIONIX_APP_ID"],
    "x-app-key": os.environ["NUTRITIONIX_API_KEY"],
}

user_input = input("Please enter the exercise(s) you performed: ")

nutritionix_exercise_parameters = {
    "query": user_input,
    "weight_kg": float(os.environ["NUTRITIONIX_WEIGHT"]),
    "height_cm": float(os.environ["NUTRITIONIX_HEIGHT"]),
    "age": int(os.environ["NUTRITIONIX_AGE"]),
}

nutritionix_response = requests.post(url=nutritionix_exercise_endpoint, headers=nutritionix_headers,
                                     json=nutritionix_exercise_parameters)
nutritionix_response.raise_for_status()

nutritionix_json = nutritionix_response.json()

sheety_endpoint = (f"https://api.sheety.co/{os.environ["SHEETY_USERNAME"]}/"
                   f"{os.environ["SHEETY_WORKOUT_PROJECT_NAME"]}/{os.environ["SHEETY_WORKOUT_SHEET_NAME"]}")

sheety_headers = {
    "Authorization": f"Bearer {os.environ["SHEETY_API_KEY"]}",
}

for exercise in nutritionix_json["exercises"]:
    exercise_date = datetime.now().strftime("%Y-%m-%d")
    exercise_time = datetime.now().strftime("%I:%M %p")
    exercise_name = exercise["name"]
    exercise_duration = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]

    sheety_parameters = {
        "workout": {
            "date": exercise_date,
            "time": exercise_time,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_parameters)
    sheety_response.raise_for_status()
