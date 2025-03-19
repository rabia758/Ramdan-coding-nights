import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.environ["GEMINI_API_KEY"]

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! I'm the Gemini Chatbot. How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)
    response_text = response.text if hasattr(response, 'text') else "No response from the model."
    await cl.Message(content=response_text).send()
    
