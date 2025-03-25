from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
template1 = PromptTemplate(
    template='generate 5 lines on the topic of {topic}',
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template='genrate the summary of the {report}',
    input_variables=["report"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = template1 | model | template2 | model | parser

result = chain.invoke({"topic": "cricket"})

print(result)

chain.get_graph().print_ascii()