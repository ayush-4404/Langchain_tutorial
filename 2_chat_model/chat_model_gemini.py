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

# Example query
# model.invoke("what is capital of india")
while True:
    question=input("enter your query: ")
    if question== "exit" : break
    response = model.generate_content(question)
    print(response)


