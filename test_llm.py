from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Initialize the ChatOpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}"
)

# Format the prompt with a predefined topic
formatted_prompt = prompt.format(topic="Python programming")

# Generate the response
response = llm.invoke(formatted_prompt)

# Print the generated content
print("Generated content:")
print(response.content) 