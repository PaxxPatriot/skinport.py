import asyncio

import skinport
from skinport import AppID


async def main():
    client = skinport.Client()
    try:
        transactions = await client.get_account_transactions(limit=10)
        for transaction in transactions:
            print(transaction.amount)
    except skinport.AuthenticationError:
        print("Authentication failed")

    items = await client.get_items(app_id=AppID.tf2)
    print(len(items))

    items = await client.get_items(app_id=AppID.csgo)
    print(len(items))

    await client.close()


asyncio.run(main())
