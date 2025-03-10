import streamlit as st  # for creating the interface
import pandas as pd  # for data manipulation
import datetime  # for handling dates
import csv  # for loading and writing CSV files
import os  # for file operations

# Configure the Streamlit app
st.set_page_config(
    page_title="Mood Tracker",
    page_icon="🌈",
    layout="wide"
)

# Define the CSV file to store mood data
MOOD_FILE = "mood_log.csv"

# Function to load mood data from the CSV file
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    try:
        mood_data = pd.read_csv(MOOD_FILE)
        # Ensure the DataFrame has the required columns
        if "Date" not in mood_data.columns or "Mood" not in mood_data.columns:
            return pd.DataFrame(columns=["Date", "Mood"])
        return mood_data
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to save mood data to the CSV file
def save_mood_data(date, mood):
    with open(MOOD_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# UI Logic
st.title("Mood Tracker 🌈")
today = datetime.date.today()

st.subheader("How are you feeling today? 👋")
mood = st.selectbox("Select your mood", ["Happy 🙂", "Sad 😞", "Angry 😠", "Neutral 😐"])

if st.button("Log Mood 🔒"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully! ☀")

# Display the mood log
st.subheader("Your Mood Log 📝")
mood_data = load_mood_data()
st.dataframe(mood_data)

# Display the mood counts as a bar chart
if not mood_data.empty:
    st.subheader("Mood Distribution 📊")
    mood_data["Date"] = pd.to_datetime(mood_data["Date"])
    mood_counts = mood_data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)

# Add footer
st.markdown("------------------")
st.subheader("Mood Trends Over Time! ✅")
st.markdown("Made with ❤ by  [Rabia Rizwan](https://github.com/rabia758)")