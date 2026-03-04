from fastapi import FastAPI
import requests
import time

app = FastAPI()

@app.get("/")
def root():
    return {"status": "EscapeRoute AI running"}

@app.get("/flight_history")
def flight_history(airport: str):

    now = int(time.time())
    five_days = now - (5 * 24 * 60 * 60)

    url = f"https://opensky-network.org/api/flights/departure?airport={airport}&begin={five_days}&end={now}"

    try:
        r = requests.get(url, timeout=20)
        flights = r.json()
    except:
        return {"error": "Unable to fetch flight history"}

    results = []

    for f in flights:

        results.append({
            "flight": f.get("callsign"),
            "origin": f.get("estDepartureAirport"),
            "destination": f.get("estArrivalAirport"),
            "departure_time": f.get("firstSeen"),
            "arrival_time": f.get("lastSeen")
        })

    return results
