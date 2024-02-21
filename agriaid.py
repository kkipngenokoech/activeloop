from api import chat
from langchain.schema import (HumanMessage, SystemMessage)


messages = [
    SystemMessage(content="Hi there! 👋 You're AgriAid, a virtual agricultural assistant. You're here to help farmers with all their farming needs and provide valuable information to make their farming journey smoother and more productive."),
    HumanMessage(content="I'm a farmer and I need help with my crops, how do i plant maize?")
]

print(chat(messages))

