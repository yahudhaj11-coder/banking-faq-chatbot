import google.generativeai as genai

API_KEY = "PASTE_YOUR_API_KEY_HERE"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

question = input("Ask a banking question: ")

response = model.generate_content(question)

print("\nAnswer:")
print(response.text)