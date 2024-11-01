import os
import requests
from datetime import date, timedelta

pixela_headers = {
    "X-USER-TOKEN": os.environ["PIXELA_TOKEN"],
}

today = date.today().strftime("%Y%m%d")
yesterday = (date.today() - timedelta(days=1)).strftime("%Y%m%d")
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y%m%d")

print(yesterday)
print(today)
print(tomorrow)

# Create user

pixela_users_endpoint = "https://pixe.la/v1/users"

pixela_user_params = {
    "token": os.environ["PIXELA_TOKEN"],
    "username": os.environ["PIXELA_USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_users_endpoint, json=pixela_user_params)
# print(response.text)

# Create graph

pixela_graphs_endpoint = f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs"

pixela_graph_params = {
    "id": "graph1",
    "name": "Graph 1",
    "unit": "thing",
    "type": "int",
    "color": "ajisai",
    "timezone": "America/Chicago",
}

# response = requests.post(url=pixela_graphs_endpoint, headers=pixela_headers, json=pixela_graph_params)
# print(response.text)

# Create pixel

pixela_pixel_post_endpoint = f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs/graph1"

pixela_pixel_post_params = {
    "date": f"{yesterday}",
    "quantity": "2",
}

# response = requests.post(url=pixela_pixel_post_endpoint, headers=pixela_headers, json=pixela_pixel_post_params)
# print(response.text)

# Update pixel

pixela_pixel_put_endpoint = f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs/graph1/{today}"

pixela_pixel_put_params = {
    "quantity": "3",
}

# response = requests.put(url=pixela_pixel_put_endpoint, headers=pixela_headers, json=pixela_pixel_put_params)

# Delete pixel

pixela_pixel_delete_endpoint = f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs/graph1/{today}"

# response = requests.delete(url=pixela_pixel_delete_endpoint, headers=pixela_headers)
# print(response.text)
