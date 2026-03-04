from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"status": "EscapeRoute AI running"}

@app.get("/escape_routes")
def escape_routes(origin: str):

    try:
        url = "https://opensky-network.org/api/states/all?lamin=20&lomin=50&lamax=30&lomax=60"

        r = requests.get(url, timeout=5)

        data = r.json()

        states = data.get("states", [])

        routes = {}

        for s in states:

            callsign = s[1]

            if not callsign:
                continue

            airline = callsign[:3]

            routes[airline] = routes.get(airline, 0) + 1

        results = [
            {"airline": k, "active_flights": v}
            for k, v in routes.items()
        ]

        results.sort(key=lambda x: x["active_flights"], reverse=True)

        return results[:10]

    except Exception as e:

        return {
            "error": "Flight data temporarily unavailable",
            "message": str(e)
        }
