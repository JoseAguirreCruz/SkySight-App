import requests

def get_flight_data(flight_number, ):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
    "access_key": "47ac311f0e565b5fb2af38c5c85f84ec", 
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
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_shipment_data(tracking_number):
    url = "https://api.ship24.com/tracking"
    params = {
        "apiKey": "apik_3rJU47UiO5lwXqtIl2VC7kYiIJXova", 
        "trackingNumber": tracking_number,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

