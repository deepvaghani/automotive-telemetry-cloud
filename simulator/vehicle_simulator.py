import time
import random
from datetime import datetime

# Initial values
speed = 0.0
latitude = 50.8321      # Example: Chemnitz
longitude = 12.9214

print("Starting vehicle telemetry simulator...\n")

while True:
    # Speed changes smoothly
    speed += random.uniform(-5, 5)
    speed = max(0, min(speed, 140))  # 0–140 km/h

    # RPM depends on speed
    rpm = int(speed * 40 + random.randint(-300, 300))
    rpm = max(800, rpm)

    # Engine temperature
    engine_temp = 70 + speed * 0.2 + random.uniform(-2, 2)

    # GPS movement
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

    print(telemetry_data)

    time.sleep(2)