from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

st.title("Research Paper Explainer")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template = load_prompt("template.json")

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.7
)

if st.button("Summarize"):
    with st.spinner("Generating response..."):
        try:
            chain = template | model

            result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            })

            content = result.content

            if isinstance(content, str):
                st.markdown(content)
            elif isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        st.markdown(item["text"])
                    elif isinstance(item, str):
                        st.markdown(item)

        except Exception as e:
            st.error(f"Error: {e}")
