import streamlit as st
import random
import time
import requests

st.set_page_config(
    page_title= "Money making Machine",
    page_icon= "💰",
    layout="wide",
)

st.title("Money Making Machine 💰")

def generate_money ():
    return random.randint(1, 1000)

st.subheader("Instant cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your Money....")
    time.sleep(2)
    amount = generate_money()
    st.success(f"You made ${amount}!🎉")

#fetech data for get side_hustle:
def fetch_side_hustle():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            advice = response.json()
            return advice["slip"]["advice"]
        else:
            return "No side hustle available"
    except Exception as e:
        return f"Something went wrong ❌: {e}"
    
st.subheader("side hustles ideas")
if st.button("Genetrate Hustle"):
    idea = fetch_side_hustle()
    st.success(f"💡 {idea}")

#fetch data to get money quotes:
def fetch_money_quotes():
    try:
        response = requests.get("https://stoic-quotes.com/api/quote")
        if response.status_code == 200:
            quote = response.json()
            return quote['text']
        else:
            return "Money Quotes Not Found!"
    except Exception as e:
        return f"Something went wrong: {e}"

st.subheader("Money Making Motivation")
if st.button("Generate Money Quotes!"):
    quote = fetch_money_quotes()
    st.info(f"💡 {quote}")



