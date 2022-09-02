import ipinfo
import asyncio
from config import ACCESS_TOKEN

handler = ipinfo.getHandlerAsync(ACCESS_TOKEN)
# >>> ip_address = '216.239.36.21'
async def do_req():
    details = await handler.getDetails(ip_address)
    print(details.city)
    print(details.loc)


loop = asyncio.get_event_loop()
loop.run_until_complete(do_req())
# Mountain View
# 37.4056,-122.0775

# >>> ip_address = '1.1.1.1'
# >>> loop.run_until_complete(do_req())
# New York City
# 40.7143,-74.0060