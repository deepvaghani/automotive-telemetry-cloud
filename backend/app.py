from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store latest telemetry data (in-memory for now)
latest_telemetry = {}

@app.route("/telemetry", methods=["POST"])
def receive_telemetry():
    global latest_telemetry
    data = request.json

    # Add server-side timestamp
    data["received_at"] = datetime.utcnow().isoformat()
    latest_telemetry = data

    return jsonify({"status": "telemetry received"}), 200

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