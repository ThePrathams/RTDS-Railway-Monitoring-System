# 🚆 RTDS: Real-Time Railway Safety System

## 📌 Overview
RTDS is an IoT-based system designed to monitor railway track conditions in real time using MQTT and ROOF computing.

## 🔄 System Workflow
Sensor → Publisher → Broker → Subscriber → Database → Dashboard

## ⚙️ Technologies Used
- Python
- MQTT (Mosquitto)
- MongoDB
- Streamlit
- ROOF Computing

## 🚀 Features
- Real-time monitoring
- Alert generation
- Live dashboard visualization
- Scalable architecture

## ▶️ How to Run
pip install -r requirements.txt  
python subscriber.py  
python publisher.py  
streamlit run dashboard.py  

## 📊 Alerts
- Vibration > 1.5 → Track damage  
- Temperature > 45°C → Overheating  
- Obstacle = 1 → Immediate alert  

## 👨‍💻 Team Members
- Prathamesh Bansode  
- Aditya Chandwade  
- Sumit Dolharkar  
- Aditya Patil
