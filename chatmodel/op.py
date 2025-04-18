from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

model=ChatOpenAI()


class Review(BaseModel):

    summary: str
    sentiment: str


structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""the product is great but the service is bad""")

print(result)


