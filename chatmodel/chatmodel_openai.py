from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

mdoel=ChatOpenAI(model='gpt-4')

result=model.invoke("what is the capital of india")

print(result)

