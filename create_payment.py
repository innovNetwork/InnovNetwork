import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

CINETPAY_API_KEY = os.getenv("CINETPAY_API_KEY")
CINETPAY_SITE_ID = os.getenv("CINETPAY_SITE_ID")
CINETPAY_URL = "https://api-checkout.cinetpay.com/v2/payment"

def create_payment(amount, currency, return_url, cancel_url, email):
    if not CINETPAY_API_KEY or not CINETPAY_SITE_ID:
        raise ValueError("Clé API ou Site ID CinetPay manquant")

    transaction_id = str(uuid.uuid4())  # Identifiant unique pour chaque transaction

    payload = {
        "amount": amount,
        "currency": currency,
        "transaction_id": transaction_id,
        "customer_name": "Client",
        "customer_surname": "InnoV",
        "customer_email": "client@innov.ci",
        "customer_phone_number": phone,
        "customer_address": "Abidjan",
        "customer_city": "Abidjan",
        "customer_country": "CI",
        "customer_state": "CI",
        "customer_zip_code": "00225",
        "return_url": return_url,
        "cancel_url": cancel_url,
        "notify_url": "https://votre-domaine.com/cinetpay-callback",  # à modifier selon ton déploiement
        "site_id": "105893723",
        "apikey": "14468589816812befc81e928.71500932",
        "lang": "fr",
        "channels": "ALL",
        "metadata": {
            "email": email
        }
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(CINETPAY_URL, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Erreur CinetPay : {response.text}")

    data = response.json()
    if data.get("code") != "201":
        raise Exception(f"Paiement refusé : {data.get('message')}")

    return {
        "payment_url": data["data"]["payment_url"],
        "transaction_id": transaction_id
    }
