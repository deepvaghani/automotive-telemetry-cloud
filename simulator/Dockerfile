FROM python:3.9-slim

WORKDIR /simulator

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "vehicle_simulator.py"]