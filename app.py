import streamlit as st
import random
import pandas as pd
import uuid
from datetime import datetime
import os

# App Title
st.title("❤️ Love Calculator ❤️")

# Inputs
name1 = st.text_input("Enter Your Name")
name2 = st.text_input("Enter Your Partner's Name")

# Create anonymous session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Function to save data
def save_data(data):
    file = "user_data.csv"

    if os.path.exists(file):
        df = pd.read_csv(file)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data])

    df.to_csv(file, index=False)

# Button action
if st.button("Calculate Love"):
    if name1 and name2:
        love_score = random.randint(50, 100)
        st.success(f"💖 Love Percentage: {love_score}%")

        user_data = {
            "session_id": st.session_state.session_id,
            "name1": name1,
            "name2": name2,
            "love_score": love_score,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        save_data(user_data)
    else:
        st.warning("Please enter both names")

# Admin Panel
st.markdown("---")
admin_password = st.text_input("Admin Password", type="password")

if admin_password == "admin123":
    st.subheader("📊 User Data")
    if os.path.exists("user_data.csv"):
        df = pd.read_csv("user_data.csv")
        st.dataframe(df)
    else:
        st.info("No data available")
