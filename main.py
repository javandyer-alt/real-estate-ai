from fastapi import FastAPI
<<<<<<< HEAD
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Deal(BaseModel):
    property: str
    tenure: str

@app.post("/analyse")
def analyse(deal: Deal):
    response = client.responses.create(
        model="gpt-5.3",
        input=f"Analyse this real estate deal: {deal.property}, tenure: {deal.tenure}"
    )
    
    return {
        "result": response.output_text
    }


