import requests
from app.schemas import Coordinates

def get_my_ip(ip: str) -> str: 
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json() 
    return data.get("query", ip) 

def get_coordinates(ip: str) -> Coordinates:
    response = requests.get(f"http://ip-api.com/json/{ip}") 
    data = response.json() 
    return Coordinates(
        ip=data.get("query", ip),
        lat=data.get("lat"),
        lon=data.get("lon")
    )

def send_to_service_b(coords: Coordinates):
    url = "http://localhost:8001/store"
    response = requests.post(url, json=coords.dict())
    return response.json()












