from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from prompts import chat


prompt = PromptTemplate(template="Question: {question}\nAnswer:", input_variables=["question"])

# llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0)
chain = LLMChain(llm=chat, prompt=prompt)

chain.run(question="What is AgriAid?")