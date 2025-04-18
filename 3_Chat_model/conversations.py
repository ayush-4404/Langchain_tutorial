from langchain_google_genai import ChatGoogleGenerativeAI as genAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage, SystemMessage

messages=[
    SystemMessage(content="You are expert in social media marketing"),
    HumanMessage(content="Give a short tip to increase engaging posts on instagram")
]
model=genAI(model="gemini-1.5-pro")
result=model.invoke(messages)
print( result.content)
