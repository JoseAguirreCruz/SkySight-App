import os
from dotenv import load_dotenv
import requests

load_dotenv()  

def get_flight_data(flight_number):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": os.getenv('AVIATIONSTACK_API_KEY'), 
        "flight_number": flight_number,
    }   
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_weather_data(city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": os.getenv('WEATHER_API_KEY'),
        "q": city,
        "days": 1,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data
