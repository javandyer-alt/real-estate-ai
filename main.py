from fastapi import FastAPI
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def home():
    return {"status": "AI running"}

@app.post("/analyse")
def analyse(deal: dict):
    prompt = "You are a UK real estate finance solicitor..."

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": str(deal)}
        ]
    )

    return {"result": response.choices[0].message.content}