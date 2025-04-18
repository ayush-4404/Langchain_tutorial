from langchain_google_genai import ChatGoogleGenerativeAI as genAI
# import os
from dotenv import load_dotenv
load_dotenv()


# # Get API Key
# API_KEY = os.getenv("GEMINI_API_KEY")

# # Configure Gemini API
# genAI.configure(api_key=API_KEY)

from langchain_core.messages import HumanMessage, SystemMessage

messages=[
    SystemMessage(content="You are expert in social media marketing"),
    HumanMessage(content="Give a short tip to increase engaging posts on instagram")
]
model=genAI(model="gemini-1.5-pro")
result=model.invoke(messages)
print( result.content)
