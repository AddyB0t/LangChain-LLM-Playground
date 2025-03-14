from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

model= ChatOpenAI()

load_dotenv()



prompt1 = PromptTemplate(
    template="Write a detailed report on the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='write a summary of the following text report on {text}',
    input_variables=["text"]
)

template1 = prompt1.invoke({"topic": "black hole"})

result = model.invoke(template1)

print(result.content)   

template2 = prompt2.invoke({"text": result.content})

result2 = model.invoke(template2)

print(result2.content)

