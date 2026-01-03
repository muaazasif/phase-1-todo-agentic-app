# run_gemini.py
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")

prompt = open("CLAUDE.md").read()
response = model.generate_content(prompt)
print(response.text)
