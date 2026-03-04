from fastapi import FastAPI
import requests
import os
from datetime import datetime, timedelta

app = FastAPI()

API_KEY = os.getenv("RAPIDAPI_KEY")

@app.get("/")
def root():
    return {"status": "EscapeRoute AI running"}

@app.get("/history")
def history(airport: str):

    today = datetime.utcnow().strftime("%Y-%m-%d")

    url = f"https://aerodatabox.p.rapidapi.com/flights/airports/iata/{airport}/{today}"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
    }

    r = requests.get(url, headers=headers)

    data = r.json()

    flights=[]

    for f in data.get("departures",[]):

        flights.append({
            "flight": f.get("flight",{}).get("iata"),
            "airline": f.get("airline",{}).get("name"),
            "destination": f.get("arrival",{}).get("airport",{}).get("iata"),
            "status": f.get("status"),
            "departure_time": f.get("departure",{}).get("scheduledTimeUtc")
        })

    return flights
