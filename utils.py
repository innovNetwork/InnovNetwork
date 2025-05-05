import random
import string
from sms import send_sms

def generer_identifiants():
    username = 'user' + ''.join(random.choices(string.digits, k=4))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return username, password
