from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

template = """Question: {question}

Answer: """
prompt = PromptTemplate(
    template=template,
    input_variables=['question']
)

# user question
question = "What is the capital city of France?"


# initialize Hub LLM
hub_llm = HuggingFaceHub(
        repo_id='google/flan-t5-large',
    model_kwargs={'temperature':0}
)

# initialize LLMChain
llm = LLMChain(
    hub=hub_llm,
    prompt_template=prompt
)

# generate response

print(llm.run(question))