import os
import time
import random
import requests

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://telemetry:3000/telemetry"
)

print("🚗 Telemetry Simulator started")
print("Backend URL:", BACKEND_URL, flush=True)

speed = 0
rpm = 1000
engine_temp = 85
lat = 50.8321
lon = 12.9214

while True:
    # Simulate real driving behavior
    speed = max(0, min(140, speed + random.randint(-2, 4)))
    rpm = max(900, min(6000, rpm + random.randint(-150, 250)))
    engine_temp = max(80, min(100, engine_temp + random.randint(-1, 1)))

    lat += random.uniform(-0.0001, 0.0001)
    lon += random.uniform(-0.0001, 0.0001)

    payload = {
        "speed_kmh": speed,
        "rpm": rpm,
        "engine_temp_c": engine_temp,
        "latitude": lat,
        "longitude": lon
    }

    try:
        r = requests.post(BACKEND_URL, json=payload, timeout=2)
        print("Sent:", payload, "Status:", r.status_code, flush=True)
    except Exception as e:
        print("❌ Error:", e, flush=True)

    time.sleep(1)
