import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient


broker = "localhost"
topic = "railway/track/data"

def analyze_data(data):
    alerts = []

    if data["vibration"] > 1.5:
        alerts.append("⚠️ High Vibration - Possible Track Damage")

    if data["temperature"] > 45:
        alerts.append("⚠️ High Temperature - Fire Risk")

    if data["obstacle"] == 1:
        alerts.append("⚠️ Obstacle Detected on Track")

    return alerts

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    print("\nReceived:", data)

    # Skip database for demo
    alerts = analyze_data(data)

    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("✅ Normal Condition")
        
client = mqtt.Client()
client.connect(broker, 1883)
client.subscribe(topic)
client.on_message = on_message

print("Subscriber Running...")
client.loop_forever()