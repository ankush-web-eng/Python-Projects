import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("../../.env")
token = os.getenv("PIXELA_TOKEN")
username = os.getenv("PIXELA_USERNAME")
graphs_id = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

today = datetime.now()

headers = {
    "X-USER-TOKEN" : token
}
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
graph_params = {
    "id" : graphs_id,
    "name": "Coding Graph",
    "unit" : "Problems",
    "type" : "int",
    "color" : "ichou"
}
# resp = requests.post(url=graph_endpoint, json=graph_params, headers=headers)


add_status = bool(input("Do you want to update today's problems? "))
if add_status:
    pixelpost_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphs_id}"
    problems = input("Enter no. of Problems you solved today: ")
    post_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity" : problems,
    }
    res = requests.post(url=pixelpost_endpoint, json=post_params, headers=headers)
    print(res.text)


update_status = bool(input("Do you want to update anything? "))
if update_status:
    date = input("Enter date to be fixed: ")
    change = input("What is the new Quantity: ")
    update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphs_id}/{date}"
    new_pixel_params = {
        "quantity" : change
    }
    respon = requests.put(url=update_endpoint,json=new_pixel_params, headers=headers)
    print(respon.text)


delete_status = bool(input("Do you want to delete anything? "))
if delete_status:
    date = input("Enter date to be fixed: ")
    delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graphs_id}/{date}"
    respons = requests.delete(url=delete_endpoint, headers=headers)
    print(respons.text)
    