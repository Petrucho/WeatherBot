from config import ACCESS_TOKEN
import ipinfo
import os

# ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
handler = ipinfo.getHandler(ACCESS_TOKEN)
#ip_address = ip.get() #'109.252.122.45' #MGTS '93.80.87.136' #beeline
def get_info(ip_address):
    details = handler.getDetails(ip_address)        
    # print(vars(details))
    return details.city, details.loc, details.country, details.region