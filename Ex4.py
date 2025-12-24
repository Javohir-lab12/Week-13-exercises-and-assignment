import requests
import json
API_URL = "http://universities.hipolabs.com/search"
country_name = input("Enter country name: ")
params = {
    "country": country_name
}
uni_list = []
response = requests.get(API_URL, params=params)
if response.status_code == 200:
    data_list = json.loads(response.text)
    for dict in data_list:
        uni_list.append(dict['name'])
    if len(uni_list) == 0:
        print(f"No universities found for {country_name}.")
    else:
        print(f"Found {len(uni_list)} universities in Uzbekistan.")
        print("Here are the first 5:")
        for i in range(1,6):
            print(f"{i}. {uni_list[i-1]}")
else:
    print("Connection error occured")