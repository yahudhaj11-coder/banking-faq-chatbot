import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Banking FAQ Assistant")

col1, col2 = st.columns(2)

with col1:
    if st.button("What is KYC?"):
        st.session_state.question = "What is KYC?"

    if st.button("What is AML?"):
        st.session_state.question = "What is AML?"

with col2:
    if st.button("What is SWIFT?"):
        st.session_state.question = "What is SWIFT?"

    if st.button("What is FATCA?"):
        st.session_state.question = "What is FATCA?"

question = st.text_input(
    "Ask a banking question",
    value=st.session_state.get("question", "")
)

SYSTEM_PROMPT = """
You are a banking assistant.

Answer banking questions professionally.

Keep answers under 150 words.

If unsure, say:
'I am not certain about that information.'

Focus on:
- KYC
- AML
- SWIFT
- Remittances
- Banking Operations
"""

if question:
    response = model.generate_content(
    SYSTEM_PROMPT + "\n\nUser Question: " + question
)
    st.write(response.text)