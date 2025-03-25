from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

template = PromptTemplate(
    template='Generate a 3 line joke'
)

parser = StrOutputParser()

# Create a chain that generates a joke and then generates another one
chain = RunnableSequence([
    template,
    model,
    parser,
    template,
    model,
    parser
])

# Invoke the chain with an empty string as input
result = chain.invoke("")
print(result)

