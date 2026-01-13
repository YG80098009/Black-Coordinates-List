from fastapi import FastAPI, HTTPException
import uvicorn
import json
import requests

app = FastAPI()
app.add_route


@app.get("/ip/{ip}")
def get_coordinats(ip):
    url = "http://ip-api.com/json/"
    json_coordinats = requests.get(url, ip)
    return json_coordinats


@app.post("/apib/{coor}")
def send_to_service_b(coor):
    x = requests.post("http://localhost:8001/store/{coor}")
    return {"message": "successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost", port="8000")


