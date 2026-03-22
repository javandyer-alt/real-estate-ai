from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Deal(BaseModel):
    property: str
    tenure: str

@app.get("/")
def home():
    return {"status": "AI running"}

@app.post("/analyse")
def analyse(deal: Deal):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"You are a UK real estate finance solicitor. Analyse this deal: {deal.property}, tenure: {deal.tenure}"
    )

    try:
        output = response.output[0].content[0].text
    except:
        output = str(response)

    return {"result": output}