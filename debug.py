import asyncio
import logging

import skinport
from collections import Counter

logger = logging.getLogger("skinport")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="skinport.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

skinport_client = skinport.Client()

c = Counter()

@skinport_client.listen("saleFeed")
async def on_sale_feed(data):
    print("New Event")
    salefeed = skinport.SaleFeed(data=data)
    for item in salefeed.sales:
        c[item.quality] += 1



if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        skinport_client.run(app_id=skinport.AppID.dota2)
    finally:
        print(c)