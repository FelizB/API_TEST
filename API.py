import requests


def ISS():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    latitude = response.json()["iss_position"]["latitude"]
    longitude = response.json()["iss_position"]["longitude"]
    return latitude, longitude

