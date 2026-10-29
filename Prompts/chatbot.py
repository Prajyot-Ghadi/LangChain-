from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

chat_history = [
    SystemMessage(content="You are a helpful AI asistent")
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))

    try:
        result = model.invoke(chat_history)

        ai_response = result.text
        print("AI:", ai_response)

        chat_history.append(AIMessage(content=ai_response))

    except Exception as e:
        print("Error:", e)
        chat_history.pop()

print(chat_history)
