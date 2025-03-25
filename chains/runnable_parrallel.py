from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

template1 = PromptTemplate(
    template="Generate a 5 line poem about {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Generate a 3 line joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = RunnableParallel({
    'poem': template1 | model | parser,
    'joke': template2 | model | parser
})

print(chain.invoke({"topic": "dogs"}))
