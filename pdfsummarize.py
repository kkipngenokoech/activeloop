from langchain import PromptTemplate, OpenAIChat
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from prompts import llm

summarize_chain = load_summarize_chain(llm)
document_loader = PyPDFLoader(file_path="data/AgriAid.pdf")
document = document_loader.load()


summary = summarize_chain(document)
print(summary['output_text'])