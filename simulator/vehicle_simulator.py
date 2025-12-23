import os
import requests
import time

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:3000/telemetry"
)

while True:
    data = {
        "speed_kmh": 60,
        "rpm": 2500,
        "engine_temp_c": 90,
        "latitude": 50.8321,
        "longitude": 12.9214
    }

    try:
        requests.post(BACKEND_URL, json=data, timeout=3)
    except Exception as e:
        print("Error:", e)

    time.sleep(1)
