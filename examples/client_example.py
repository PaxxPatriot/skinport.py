import asyncio
from collections import Counter

import skinport
from skinport.enums import AppID


async def main():
    client = skinport.Client()
    counter = Counter()
    await client.login()
    try:
        transactions = await client.get_account_transactions(limit=10)
        for transaction in transactions:
            print(transaction.type)
            for item in transaction.items:
                counter[item.buyer_country] += 1
    except skinport.AuthenticationError:
        print("Authentication failed")

    print(counter)

    items = await client.get_items(app_id=AppID.tf2)
    print(len(items))

    items = await client.get_items(app_id=AppID.csgo)
    print(len(items))

    await client.close()


asyncio.run(main())
