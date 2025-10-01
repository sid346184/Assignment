import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="deepseek-r1-distill-llama-70b",
    reasoning_format="parsed",
    max_tokens=1000,
    temperature=0.7,
)

messages = [
    SystemMessage(content="You are a helpful AI assistant. Answer clearly and politely.")
]

def chatbot(user_input: str):
    messages.append(HumanMessage(content=user_input))  
    response = llm.invoke(messages)                  
    messages.append(AIMessage(content=response.content)) 
    return response.content
