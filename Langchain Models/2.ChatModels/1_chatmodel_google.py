from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash',  temperature=0)

result = model.invoke("Tell me about Virat Kohali")

for block in result.content:
    if isinstance(block, dict) and block.get("type") == "text":
        print(block["text"])