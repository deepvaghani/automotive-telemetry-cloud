from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Store latest telemetry data (in-memory for now)
latest_telemetry = {}

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/telemetry", methods=["POST"])
def receive_telemetry():
    global latest_data
    data = request.json

    latest_telemetry = {
        "speed": data.get("speed_kmh"),
        "rpm": data.get("rpm"),
        "engine_temp": data.get("engine_temp_c"),
        "lat": data.get("latitude"),
        "lon": data.get("longitude"),
        "received_at": data.get("received_at")
    }
    return {"status": "ok"}

@app.route("/telemetry", methods=["GET"])
def get_telemetry():
    if not latest_telemetry:
        return jsonify({"message": "No telemetry received yet"}), 404
    return jsonify(latest_telemetry), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "backend running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)