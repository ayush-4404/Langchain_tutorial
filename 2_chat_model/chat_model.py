
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

messages=[
    SystemMessage("You are expert in social media marketing"),
    HumanMessage("Give a short tip to increase engaging posts on instagram")
]

result=model.generate_content(messages)
print(result.text)


