from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "EscapeRoute AI running"}

@app.get("/escape_routes")
def escape_routes(origin: str):

    url = "https://opensky-network.org/api/states/all"

    r = requests.get(url)
    data = r.json()

    states = data.get("states", [])

    routes = {}

    for s in states:

        callsign = s[1]

        if not callsign:
            continue

        airline = callsign[:3]

        if airline not in routes:
            routes[airline] = 0

        routes[airline] += 1

    results = []

    for r in routes:
        results.append({
            "airline": r,
            "active_flights": routes[r]
        })

    results.sort(key=lambda x: x["active_flights"], reverse=True)

    return results[:10]
