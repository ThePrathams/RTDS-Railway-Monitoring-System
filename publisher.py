import paho.mqtt.client as mqtt
import json
import time
from sensor_simulator import generate_sensor_data

broker = "localhost"
port = 1883
topic = "railway/track/data"

client = mqtt.Client()
client.connect(broker, port)

print("Publisher Running...")

while True:
    data = generate_sensor_data()
    message = json.dumps(data)
    client.publish(topic, message)
    print("Published:", message)
    time.sleep(2)