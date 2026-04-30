import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.set_page_config(page_title="RTDS Dashboard", layout="wide")
st.title("🚆 RTDS Railway Safety Dashboard")

client = MongoClient("mongodb://localhost:27017/")
db = client["railway_db"]
collection = db["track_data"]

data = list(collection.find({}, {"_id": 0}))

if data:
    df = pd.DataFrame(data)

    st.subheader("📋 Live Data")
    st.dataframe(df.tail(10))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌡 Temperature")
        st.line_chart(df["temperature"])

    with col2:
        st.subheader("📈 Vibration")
        st.line_chart(df["vibration"])

    latest = df.iloc[-1]

    st.subheader("🚨 Current Status")

    if latest["obstacle"] == 1:
        st.error("Obstacle Detected!")
    elif latest["vibration"] > 1.5:
        st.warning("High Vibration!")
    elif latest["temperature"] > 45:
        st.warning("High Temperature!")
    else:
        st.success("All Systems Normal")

else:
    st.info("Waiting for sensor data...")