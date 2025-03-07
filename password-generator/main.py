import streamlit as st
import random
import string

st.set_page_config(
    page_title="password generator",
    page_icon="🔑",
    layout="centered"
)

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Letters (uppercase and lowercase)

    if use_digits:
        characters += string.digits  # Add digits (0-9)

    if use_special:
        characters += string.punctuation  # Add special characters (!@#$%^&*)

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit app
st.title("Password Generator 🔑")

# Password length slider
length = st.slider("Select Password Length", min_value=6, max_value=22, value=12)

# Checkboxes for including digits and special characters
use_digits = st.checkbox("Include Digits (0-9)")
use_special = st.checkbox("Include Special Characters (!@#$%^&*)")

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success("Password Generated Successfully! 🎉")
    st.code(password)  # Display the password in a code block for better readability

# Footer
st.write("-------------------------------")
st.write("Built With ❤ by [**Rabia Rizwan**](https://github.com/rabia758)")
