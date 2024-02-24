from api import chat
from langchain.schema import (HumanMessage, SystemMessage)



def chat_with_farmer(farmer_message):
    messages = [
        SystemMessage(content="Hi there! 👋 You're AgriAid, a virtual agricultural assistant. You're here to help farmers with all their farming needs and provide valuable information to make their farming journey smoother and more productive."),
        HumanMessage(content=farmer_message)
    ]
    return  chat(messages).content

#print(chat_with_farmer("I want to grow tomatoes"))