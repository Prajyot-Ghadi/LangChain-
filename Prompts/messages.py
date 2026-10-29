from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

messages = [
    SystemMessage(content='Your are a helpful asistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.text))

print(messages)