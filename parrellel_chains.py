from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()


model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name='claude-3-sonnet-20240229')

template1 = PromptTemplate(
    template='generate short notes on the topic of {topic}',
    input_variables=["topic"]
)    


template2 = PromptTemplate(
    template='generate a small quiz on the topic of {topic}',
    input_variables=["topic"]
)

template3 = PromptTemplate(
    template='merge the following notes and quiz: \nNotes: {notes}\nQuiz: {quiz}',
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': template1 | model1 | parser,
    'quiz': template2 | model2 | parser
})

chain = parallel_chain | template3 | model1 | parser

result = chain.invoke({"topic": "cricket"})

print(result)

chain.get_graph().print_ascii()
