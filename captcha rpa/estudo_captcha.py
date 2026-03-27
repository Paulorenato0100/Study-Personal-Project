import requests
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
recaptcha_secret = os.getenv("RECAPTCHA_SECRET")

class Formdata(BaseModel):
    name : str
    email: str
    token: str

def verifyrecap(token: str):
    url = "https://www.google.com/recaptcha/api/siteverify"

    payload = {
        "secret": recaptcha_secret,
        "response": token   
    }
    response = requests.post(url, data=payload)
    return response.json

@app.post("/submit")
def submitform(data= Formdata):
    result = verifyrecap(data.token)

    if not result.get("success"):
        raise HTTPException(status_code=400, detail="reCaptcha invalido")

    score = result.get("score",0)

    if score < 0.7:
        raise HTTPException(status_code=403, detail="score suspeito")
    
    return {"message": "Formulario aceito"}
