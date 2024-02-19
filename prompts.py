from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    ChatPromptTemplate
)
from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# this is an instance of open ai model
chat = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

template = "Hi there! 👋 You're AgriAid, a virtual agricultural assistant. You're here to help farmers with all their farming needs and provide valuable information to make their farming journey smoother and more productive."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

# human template
farmer_template = "I'm a farmer and I need help with my crops, how do i plant {crop}?"
human_message_prompt = HumanMessagePromptTemplate.from_template(farmer_template)
#chat_prompt = ChatPromptTemplate(system_message_prompt=system_message_prompt,human_message_prompt= human_message_prompt)
chat_prompt = ChatPromptTemplate(messages=[system_message_prompt, human_message_prompt])
response = chat(chat_prompt.format_prompt(crop="maize").to_messages())
print(response.content)