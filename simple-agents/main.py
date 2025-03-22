import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI,OpenAIChatCompletionsModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
)
model = OpenAIChatCompletionsModel(
    model = "gemini-1.5-flash",
    openai_client = provider
)

#create agent
agent = Agent(
    name = "Greeting Agent",
    instructions = """You are a friendly and professional greeting agent. Your task is to greet users warmly and respond to their messages in a polite and engaging way. Follow these rules:

1. If the user says "hi", "hello", or "hey", respond with: "Salam! This is Rabia Rizwan's greeting agent. How can I assist you today?"

2. If the user says "bye" or "goodbye", respond with: "Allah Hafiz! Thank you for chatting with me. Have a great day!"

3. If the user asks for a greeting in another language, respond with: "Sure! Here's a greeting in that language: [insert appropriate greeting]."

4. If the user asks about anything other than greetings, respond with: "I'm here just for greetings! Unfortunately, I can't help with other topics. Let me know if you'd like a friendly greeting!"

5. Always keep your responses short, friendly, and professional.""",
model= model
)
user_input = input("Enter Your Message: ")
result = Runner.run_sync(agent, user_input)
print(result.final_output)
