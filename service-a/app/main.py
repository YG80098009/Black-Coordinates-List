from fastapi import FastAPI, HTTPException
from services import Routs
import uvicorn
import json
import requests

app = FastAPI()
app.add_route


@app.get("/ip/{ip}")
def get_coordinats(ip):
    url =f"http://ip-api.com/json/{ip}"
    json_coordinats = requests.get(url)
    status = json_coordinats.json()
    clean_data = Routs.cleaning_data(status)
    status_server_b = Routs.send_to_server_b(clean_data)
    return {"message": "status_server_b",
            "data": clean_data}


@app.post("/store/{coor}")
def send_to_service_b(coor):
    x = requests.post("http://localhost:8001/store/{coor}")
    return {"message": "successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost", port="8000")