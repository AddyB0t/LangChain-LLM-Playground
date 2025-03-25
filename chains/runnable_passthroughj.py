from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

template = PromptTemplate(
    template='Generate a 3 line joke on the topic {topic}'
)

parser = StrOutputParser()

# Create a chain that generates a joke and then generates another one
chain1 = RunnableSequence(template, model, parser)

runnable_pass= RunnableParallel({
    'joke': chain1,
    'topic': RunnablePassthrough()
})

print(runnable_pass.invoke({'topic': 'dogs'}))

