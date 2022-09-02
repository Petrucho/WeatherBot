from config import ACCESS_TOKEN
import ipinfo
import os

# ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
handler = ipinfo.getHandler(ACCESS_TOKEN)

def get_info(ip_address):
    details = handler.getDetails(ip_address)
    return details.city, details.loc