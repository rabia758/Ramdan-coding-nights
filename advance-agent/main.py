import os
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
from dotenv import load_dotenv
from typing import Optional, Dict

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize the provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Initialize the model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider
)

# Define function tools
@function_tool("get_weather")
def get_weather(location: str, unit: str = 'C') -> str:
    """
    Fetch the weather for a given location and return the weather.
    """
    return f"The weather in {location} is 22 degrees {unit}."

@function_tool("Rabia_data")
def Rabia_data() -> str:
    """
    Fetches profile data from Rabia's API endpoint.
    """
    import requests
    url = "https://github.com/rabia758"
    response = requests.get(url)
    return response.text

@function_tool("get_time")
def get_time(location: str) -> str:
    """
    Fetch the current time for a given location.
    """
    return f"The current time in {location} is 12:00 PM."

@function_tool("translate_text")
def translate_text(text: str, target_language: str) -> str:
    """
    Translate text into the target language.
    """
    # Placeholder for translation logic (replace with actual API call)
    return f"Translated '{text}' to {target_language}: [Translation]"

@function_tool("tell_joke")
def tell_joke() -> str:
    """
    Tell a random joke.
    """
    import random
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    return random.choice(jokes)

@function_tool("get_news")
def get_news() -> str:
    """
    Fetch the latest news headlines.
    """
    # Placeholder for news API call (replace with actual API integration)
    return "Latest news: [Headline 1], [Headline 2], [Headline 3]"

# Create agents
greeting_agent = Agent(
    name="Greeting Agent",
    instructions="""
You are a friendly and professional greeting agent. Your task is to greet users warmly and respond to their messages in a polite and engaging way. Follow these rules:

1. If the user says "hi", "hello", or "hey", respond with: "Salam! This is Rabia Rizwan's greeting agent. How can I assist you today?"

2. If the user says "bye" or "goodbye", respond with: "Allah Hafiz! Thank you for chatting with me. Have a great day!"

3. If the user asks for a greeting in another language, respond with: "Sure! Here's a greeting in that language: [insert appropriate greeting]."

4. If the user asks about anything other than greetings, respond with: "I'm here just for greetings! Unfortunately, I can't help with other topics. Let me know if you'd like a friendly greeting!"

5. Always keep your responses short, friendly, and professional.
6. If the user asks for the weather, use the `get_weather` tool to fetch the weather.
    """,
    model=model,
    tools=[get_weather]
)

weather_agent = Agent(
    name="Weather Agent",
    instructions="""
You are a weather agent. Your task is to provide accurate weather information for any location requested by the user. Use the `get_weather` tool to fetch the weather data.
    """,
    model=model,
    tools=[get_weather]
)

profile_agent = Agent(
    name="Profile Agent",
    instructions="""
You are a profile agent. Your task is to fetch and display profile data for Rabia Rizwan. Use the `Rabia_data` tool to retrieve the profile information.
    """,
    model=model,
    tools=[Rabia_data]
)

time_agent = Agent(
    name="Time Agent",
    instructions="""
You are a time agent. Your task is to provide the current time for any location requested by the user. Use the `get_time` tool to fetch the time data.
    """,
    model=model,
    tools=[get_time]
)

translation_agent = Agent(
    name="Translation Agent",
    instructions="""
You are a translation agent. Your task is to translate text into the target language requested by the user. Use the `translate_text` tool to perform translations.
    """,
    model=model,
    tools=[translate_text]
)

joke_agent = Agent(
    name="Joke Agent",
    instructions="""
You are a joke agent. Your task is to tell jokes to entertain the user. Use the `tell_joke` tool to fetch a random joke.
    """,
    model=model,
    tools=[tell_joke]
)

news_agent = Agent(
    name="News Agent",
    instructions="""
You are a news agent. Your task is to fetch the latest news headlines and share them with the user. Use the `get_news` tool to retrieve the news.
    """,
    model=model,
    tools=[get_news]
)

# Chainlit OAuth callback
@cl.oauth_callback
async def callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    """
    Handle the OAuth callback from GitHub.
    Return a user object if authentication is successful, otherwise return None.
    """
    print(f"Provider ID: {provider_id}")
    print(f"User data: {raw_user_data}")
    return default_user

# Chainlit chat start
@cl.on_chat_start
async def start():
    """
    This is called when the user clicks on the start button.
    """
    cl.user_session.set("history", [])
    cl.user_session.set("agents", {
        "greeting_agent": greeting_agent,
        "weather_agent": weather_agent,
        "profile_agent": profile_agent,
        "time_agent": time_agent,
        "translation_agent": translation_agent,
        "joke_agent": joke_agent,
        "news_agent": news_agent
    })
    await cl.Message(content="Hello! I'm the Agent Auth Chatbot. How can I help you today?").send()

# Chainlit message handler
@cl.on_message
async def handle_message(message: cl.Message):
    """
    This is called when the user sends a message.
    """
    history = cl.user_session.get("history")
    agents = cl.user_session.get("agents")

    # Append user message to history
    history.append({"role": "user", "content": message.content})

    # Determine which agent to use based on the user's input
    if "weather" in message.content.lower():
        agent = agents["weather_agent"]
    elif "profile" in message.content.lower():
        agent = agents["profile_agent"]
    elif "time" in message.content.lower():
        agent = agents["time_agent"]
    elif "translate" in message.content.lower():
        agent = agents["translation_agent"]
    elif "joke" in message.content.lower():
        agent = agents["joke_agent"]
    elif "news" in message.content.lower():
        agent = agents["news_agent"]
    else:
        agent = agents["greeting_agent"]

    # Run the agent
    result = await cl.make_async(Runner.run_sync)(agent, input=history)
    response_text = result.final_output

    # Send the response
    await cl.Message(content=response_text).send()

    # Append assistant response to history
    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)

# Chainlit chat end
@cl.on_chat_end
async def end():
    """
    This is called when the user ends the chat.
    """
    print("Chat ended")