import random
import time

def generate_sensor_data():
    return {
        "track_id": "T101",
        "temperature": random.randint(20, 50),
        "vibration": round(random.uniform(0.1, 2.0), 2),
        "obstacle": random.choice([0, 1]),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }