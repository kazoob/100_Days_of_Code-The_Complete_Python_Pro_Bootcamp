import os
import requests

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

response = requests.post(url=nutritionix_exercise_endpoint, headers=nutritionix_headers,
                         json=nutritionix_exercise_parameters)
response.raise_for_status()

print(response.json())
