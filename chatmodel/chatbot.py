from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
    user_input = input(" You: ")
    chat_history.append(f"You: {user_input}")
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(f"AI: {result.content}")
    print("AI:", result.content)  # Access the content property
print(chat_history)