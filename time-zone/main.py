import streamlit as st
from datetime import datetime, time
from zoneinfo import ZoneInfo

# Configure Streamlit app
st.set_page_config(page_title="Time Zone App", page_icon=":watch:", layout="centered")

# List of timezones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "Africa/Cairo",
    "Asia/Shanghai",
    "Asia/Tokyo",
    "Asia/Dubai",
]

# Streamlit app title
st.title("Time Zone Converter ⌚")

# Multiselect for timezones
selected_timezone = st.multiselect(
    "Select a timezone", 
    TIME_ZONES, 
    default=["UTC", "Asia/Karachi"]  # Default selected timezones
)

# Display current time in selected timezones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

# Time conversion section
st.subheader("Convert Time Between Timezones 🥨")
current_time = st.time_input("Current Time", value=datetime.now().time())
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    try:
        # Get today's date
        today = datetime.today().date()
        # Combine today's date with the selected time and set the "from" timezone
        dt = datetime.combine(today, current_time).replace(tzinfo=ZoneInfo(from_tz))
        # Convert the time to the "to" timezone
        converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime('%Y-%m-%d %I:%M:%S %p')
        # Display the converted time
        st.success(f"Converted time in {to_tz}: {converted_time}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
st.subheader("Timezone Information 📍")
st.write(""" This App allow you to convert time between different timezones and display current time in selected timezone """)
st.write("Developed by [Rabia Rizwan](https://github.com/rabia758)")       