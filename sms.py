import africastalking
import os
from dotenv import load_dotenv

load_dotenv()  # charge les variables d’environnement

africastalking.initialize(
    username=os.getenv("AT_USERNAME"),
    api_key=os.getenv("AT_API_KEY")
)

sms = africastalking.SMS

def send_sms(phone, message):
    response = sms.send(message, [phone])
    return response
