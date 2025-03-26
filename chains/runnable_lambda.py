from langchain.schema.runnable import RunnableLambda
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableSequence
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()


def word_counter(text):
    return len(text.split())


template= PromptTemplate(
    template= 'Write a joke about {topic}',
    input_variables=["topic"]
)


parser= StrOutputParser()

joke_chain = RunnableParallel({
    'joke': RunnableSequence(template | model | parser),
    'word_count': RunnableSequence(template | model | parser | RunnableLambda(word_counter))
})

result=joke_chain.invoke({'topic': 'elephants'})

print(result)






