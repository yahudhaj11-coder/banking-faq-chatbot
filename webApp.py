import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Banking FAQ Assistant")

question = st.text_input("Ask a banking question")

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