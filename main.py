from fastapi import FastAPI, HTTPException, Request
from create_payment import create_payment  # Tu dois avoir ce fichier (ou ajouter la fonction ici)
import os

app = FastAPI()

@app.post("/payer")
async def payer(request: Request):
    data = await request.json()

    amount = data.get("amount")
    currency = data.get("currency", "XOF")
    return_url = data.get("return_url")
    cancel_url = data.get("cancel_url")
    email = data.get("email")

    if not all([amount, return_url, cancel_url, email]):
        raise HTTPException(status_code=400, detail="Tous les champs sont requis.")

    try:
        response = create_payment(amount, currency, return_url, cancel_url, email)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur de paiement : {str(e)}")
