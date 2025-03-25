from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="Write a short blog on the topic {product}"
)

topic = input('Enter a topic for the blog: ')

formatted_prompt = prompt.format(product=topic)


blog_title = llm.invoke(formatted_prompt)


print(f"Generated blog: {blog_title.content}")

