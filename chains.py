from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

prompt = PromptTemplate(
    template='generate 5 lines on the topic of {topic}',
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "cricket"})

print(result)

chain.get_graph().print_ascii()
