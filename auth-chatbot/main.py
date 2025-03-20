import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional,Dict

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

@cl.oauth_callback
async def callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str,str],
    default_user: cl.User,
     ) -> Optional[cl.User]:
    """
    handle the OAUTH callback from github
    Return a user object if the user is authentication is successful, otherwise return None
    """
    print(f"Provider ID: {provider_id}")
    print(f"User data: {raw_user_data}")
    return default_user

@cl.on_chat_start
async def start():
    cl.user_session.set("history",[])
    """
    This is called when the user clicks on the start button
    """
    await cl.Message(content="Hello! I'm the Auth Chatbot. How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    """
    This is called when the user sends a message
    """
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    formatted_history = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "model"
        formatted_history.append({"role":role, 'parts': [{'text': msg['content']}]})
    response = model.generate_content(formatted_history)
    response_text = response.text if hasattr(response, 'text') else ""
    history.append({'role': "assistant", 'content': response_text})
    cl.user_session.set("history", history)
    await cl.Message(content=response_text).send()

@cl.on_chat_end
async def end():
    """
    This is called when the user ends the chat
    """
    print("Chat ended")

