import requests

def get_city_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name" : city_name
    }
    try:
        response = requests.get(url, params = params)
        data = response.json()
        if len(data["results"]) == 0:
            print("City not found")
            return None, None
        city = data["results"][0]
        return city["latitude"], city["longitude"]
    except requests.exceptions.RequestException:
        print("Error accessing geocoding API")
        return None, None

def get_weather_data(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude" : latitude,
        "longitude" : longitude,
        "daily" : "temperature_2m_max,temperature_2m_min",
        "timezone" : "auto"
    }
    try:    
        response = requests.get(url, params = params)
        return response.json()
    except requests.exceptions.RequestException:
        print("Error accessing weather API")
        return None
def process_weather_data(weather_data):
    daily = weather_data["daily"]
    dates = daily["time"]
    max_temps = daily["temperature_2m_max"]
    min_temps = daily["temperature_2m_min"]
    avg_temp = sum(max_temps)/len(max_temps)
    hottest_day = dates[max_temps.index(max(max_temps))]
    coldest_day = dates[min_temps.index(min(min_temps))]
    return avg_temp, hottest_day, coldest_day
def display_results(city, avg_temp, hottest_day, coldest_day):
    print("Weather analysis result")
    print("-"*40)
    print(f"City: {city}")
    print(f"Average maximum temperatures: {avg_temp:.2f}")
    print(f"Hottest day: {hottest_day}")
    print(f"Coldest day: {coldest_day}")
def save_to_file(city, avg_temp, hottest_day, coldest_day):
    with open("weather_report.txt", "w") as file:
        file.write(f"Weather report for city {city}\n")
        file.write("-"*40+"\n")
        file.write(f"Average maximum temperatures: {avg_temp:.2f}\n")
        file.write(f"Hottest day: {hottest_day}\n")
        file.write(f"Coldest day: {coldest_day}")
    print("Result saved to weather_report.txt")
def main():
    print("Open-Meteo Weather & Climate analyzer")
    city_name = input("Enter city name:").strip()
    if not city_name:
        print("City name cannot be empty.")
        return
    latitude, longitude = get_city_coordinates(city_name)
    if latitude is None or longitude is None:
        return
    weather_data = get_weather_data(latitude, longitude)
    if weather_data is None:
        return 
    avg_temp, hottest_day, coldest_day = process_weather_data(weather_data)
    display_results(city_name, avg_temp, hottest_day, coldest_day)
    save_to_file(city_name, avg_temp, hottest_day, coldest_day)
main()