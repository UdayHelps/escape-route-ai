import requests
import time

while True:

    r=requests.get("https://opensky-network.org/api/states/all")

    data=r.json()

    flights=data["states"]

    print("Flights detected:",len(flights))

    time.sleep(300)
