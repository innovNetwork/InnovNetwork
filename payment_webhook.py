from fastapi import FastAPI, Request
from mikrotik import create_user
from create_payment import create_payment
from sms import send_sms
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API InnoV'Network"}

@app.post("/cinetpay-callback")
async def cinetpay_callback(request: Request):
    payload = await request.json()

    if payload.get("transaction_status") == "ACCEPTED":
        username = payload.get("cpm_trans_id")
        password = payload.get("cpm_trans_id")
        profile = payload.get("cpm_custom")
        phone = payload.get("phone_prefixe") + payload.get("cel_phone_num")

         # 🔒 Essaye de créer l’utilisateur MikroTik, mais ne bloque pas si ça échoue
    try:
        create_user(username, password, profile)
    except Exception as e:
        print(f"Erreur lors de la création d'utilisateur MikroTik : {e}")

    # ✅ Envoi du SMS même si MikroTik échoue
    message = f"Bienvenue sur InnoV'Network !\nLogin: {username}\nPassword: {password}"
    send_sms(phone, message)

    return {"status": "ok"}
