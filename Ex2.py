import requests
import json
url = "http://api.open-notify.org/iss-now.json"
print("Connecting to ISS satellite...")
response = requests.get(url)
if response.status_code == 200:
    print("Connected succedfully")
    python_dict = json.loads(response.text()) # python_dict = json(response) is also possible
    latitude = python_dict["iss_position"]["latitude"]
    longitude = python_dict["iss_position"]["longitude"]
    print("Current location:")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Connextion error occured")