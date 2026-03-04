from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def root():
    return {"status": "EscapeRoute AI running"}

@app.get("/escape_routes")
def escape_routes(origin: str):

    airlines = [
        "Emirates",
        "Qatar Airways",
        "Air India",
        "IndiGo",
        "Turkish Airlines",
        "Etihad",
        "Lufthansa"
    ]

    results = []

    for a in airlines:

        flights = random.randint(1,15)

        results.append({
            "airline": a,
            "active_flights": flights,
            "chance_of_flying": flights * 6,
            "chance_of_cancel": 100 - flights * 6
        })

    results.sort(key=lambda x: x["active_flights"], reverse=True)

    return results
