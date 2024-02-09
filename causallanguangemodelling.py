from langchain.llms import OpenAI

# Create a new instance of the OpenAI class
openai = OpenAI(model="gpt-3.5-turbo", temperature=0.5, max_tokens=100), 
text = "What is the meaning of life?"
response = openai(text)
