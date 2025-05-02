from fastapi import FastAPI, Request
from app.mikrotik import create_user
from app.sms import send_sms
import os

app = FastAPI()

@app.post("/cinetpay-callback")
async def cinetpay_callback(request: Request):
    payload = await request.json()

    if payload.get("transaction_status") == "ACCEPTED":
        username = payload.get("cpm_trans_id")
        password = payload.get("cpm_trans_id")
        profile = payload.get("cpm_custom")
        phone = payload.get("phone_prefixe") + payload.get("cel_phone_num")

        create_user(username, password, profile)

        message = f"Bienvenue sur InnoV'Network !\nLogin: {username}\nPassword: {password}"
        send_sms(phone, message)

    return {"status": "ok"}
