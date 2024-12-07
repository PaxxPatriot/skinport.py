import skinport

client = skinport.Client()


@client.listen("saleFeed")
async def on_sale_feed(data):
    salefeed = skinport.SaleFeed(data=data)
    sales = salefeed.sales

    print(f"Event Type: {salefeed.event_type}")
    # For more attributes check out the documentation: https://paxxpatriot.github.io/skinport.py/api.html#skinport.SaleFeedSale
    print(f"Market Hash Names: {", ".join([sale.market_hash_name for sale in sales])}")


@client.listen("maintenanceUpdated")
async def on_maintenance_updated(data):
    print(data)


@client.listen("steamStatusUpdated")
async def on_steam_status_updated(data):
    print(data)


client.run()
