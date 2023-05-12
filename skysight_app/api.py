import json
import requests

def get_flight_data(flight_number, ):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
    "access_key": "6c92ed3a525fd8fd39e0ccd083799eab", 
    "flight_number": flight_number,
    }   
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_weather_data(city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": "8594dc8ba1264ad0964173454230905",
        "q": city,
        "days": 1,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data




