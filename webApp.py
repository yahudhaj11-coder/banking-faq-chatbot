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

if question:
    response = model.generate_content(question)
    st.write(response.text)