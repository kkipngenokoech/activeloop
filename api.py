from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
telegram_token = os.getenv("token")

models = ["gpt-3.5-turbo", "gpt-3.5-turbo-instruct", "gpt-3.5-turbo-instruct-davinci", 'gpt-4']
# this is an instance of open ai model
chat = ChatOpenAI(model=models[0], openai_api_key=openai_api_key, temperature=0)
