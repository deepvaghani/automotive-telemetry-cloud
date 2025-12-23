import time
import random
import requests
from datetime import datetime

API_URL = "http://98.82.133.155:3000/telemetry"

speed = 0.0
latitude = 50.8321
longitude = 12.9214

print("Vehicle telemetry simulator started...\n")

while True:
    speed += random.uniform(-5, 5)
    speed = max(0, min(speed, 140))

    rpm = int(speed * 40 + random.randint(-300, 300))
    rpm = max(800, rpm)

    engine_temp = 70 + speed * 0.5 + random.uniform(-2, 2)

    latitude += random.uniform(-0.0003, 0.0003)
    longitude += random.uniform(-0.0003, 0.0003)

    telemetry_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "speed_kmh": round(speed, 1),
        "rpm": rpm,
        "engine_temp_c": round(engine_temp, 1),
        "latitude": round(latitude, 6),
        "longitude": round(longitude, 6)
    }

    try:
        response = requests.post(API_URL, json=telemetry_data)
        print("Sent:", telemetry_data, "| Status:", response.status_code)
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(2)
