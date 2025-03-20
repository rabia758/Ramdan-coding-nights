import streamlit as st
import requests
from fastapi import FastAPI

app = FastAPI()
random_joke = [
    {
        "setup": "Why did the chicken cross the road in Karachi?", 
        "punchline": "To escape the traffic jam!"
    },
    {
        "setup": "What do you call a Pakistani who loves tea?", 
        "punchline": "A chai-oholic!"
    },
    {
        "setup": "Why did the gol gappa wala close his shop?", 
        "punchline": "Because he ran out of 'paani' and couldn't handle the 'drama'!"
    },
    {
        "setup": "What do you call a Pakistani who can't stop talking?", 
        "punchline": "A 'baat ka patang'!"
    },
    {
        "setup": "Why did the Lahori go to the gym?", 
        "punchline": "To work on his 'buttay' (biceps)!"
    },
    {
        "setup": "What do you call a Pakistani who loves biryani?", 
        "punchline": "A 'biryani lover' with extra 'aloo'!"
    },
    {
        "setup": "Why did the Pakistani bring a ladder to the cricket match?", 
        "punchline": "To climb up the 'sixer' count!"
    },
    {
        "setup": "What do you call a Pakistani who can't decide between chai and coffee?", 
        "punchline": "A 'chai-fee'!"
    },
    {
        "setup": "Why did the Pakistani student bring a ladder to school?", 
        "punchline": "Because he wanted to go to 'high' school!"
    },
    {
        "setup": "What do you call a Pakistani who loves rain?", 
        "punchline": "A 'barish ka deewana'!"
    }
]
@app.get("/random_joke")
def get_random_joke():
    """Fetch a random joke from the Api"""
    try:
        response = requests.get("http://127.0.0.1:8000/random_joke")
        if response.status_code == 200:
         joke = response.json()
         return f"{joke["setup"]}\n\n {joke["punchline"]}"
        else:
            return "Failed to fetch a joke. Please try again."
    except Exception as e:
        return "why did yoou programmer quit his joke? \n because he didn't get a response from the API"

def main():
    st.title("Joke Generator")
    st.write("Click the button below to generate a random joke")
    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.success(joke)
    st.divider()
    st.markdown(
        """
        <div style="text-align: center;">
        <p>Joke from official joke api</p>
        <p>Build with ❤️ by <a href="https://github.com/rabia758">Rabia Rizwan</a>with streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )    

if __name__ == "__main__":
    main()
