from langchain.prompts import ChatPromptTemplate
from langchain.prompts.messenger import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Initialize chat history with proper message objects
chat_history = [
    HumanMessage(content="Hi, I need help with my order"),
    AIMessage(content="Hello! I'd be happy to help you with your order. What's your order number?")
]

# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history, 
    "query": "Where is my refund"
})

print(prompt)