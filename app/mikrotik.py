import routeros_api
import os
from sms import send_sms

def create_user(username, password, profile):
    connection = routeros_api.RouterOsApiPool(
        host=os.getenv("MIKROTIK_HOST"),
        username=os.getenv("MIKROTIK_USERNAME"),
        password=os.getenv("MIKROTIK_PASSWORD"),
        port=int(os.getenv("MIKROTIK_PORT")),
        plaintext_login=True
    )
    api = connection.get_api()
    hotspot_user = api.get_resource('/ip/hotspot/user')
    hotspot_user.add(name=username, password=password, profile=profile)
    connection.disconnect()
