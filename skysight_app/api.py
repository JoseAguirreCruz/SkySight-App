import requests

def get_flight_data(flight_number):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": "47ac311f0e565b5fb2af38c5c85f84ec", 
        "flight_iata": flight_number,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data
