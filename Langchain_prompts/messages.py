from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history=[]

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about langchain in 1 line')
]

result=model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)