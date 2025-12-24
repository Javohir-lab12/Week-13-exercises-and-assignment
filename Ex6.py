import requests
import json
API_URL = "https://randomuser.me/api/?results=10&nat=us"
response = requests.get(API_URL)
print("Fetching data from API...")
if response.status_code == 200:
    print("Successfully fetched 10 users.")
    data_list = json.loads(response.text)
    user_data = data_list["result"]
    first_name = user_data["name"]["first"]
    last_name = user_data["name"]["last"]
    email = user_data["email"]
    location = user_data["location"]["city"]
    print("Writing to fake_users.csv...")
    with open("fake_users.csv", "w") as file:
        file.write("first_name,last_name,email,city")
        for i in range(10):
            file.write(f"{first_name},{last_name},{email},{location}")
# {
#   "results": [
#     {
#       "name": { "first": "brad", "last": "gibson" },
#       "email": "brad.gibson@example.com",
#       "location": { "city": "kilcoole", ... }
#     }
#   ]
# }