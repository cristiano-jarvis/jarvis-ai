from fastapi import FastAPI
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
   return {"status": "Jarvis online 🚀"}

@app.get("/ask")
def ask(q: str):
   response = client.chat.completions.create(
       model="gpt-4.1-mini",
       messages=[
           {"role": "system", "content": "Sei Jarvis, assistente intelligente."},
           {"role": "user", "content": q}
       ]
   )
   return {"response": response.choices[0].message.content}
