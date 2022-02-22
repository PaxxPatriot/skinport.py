import skinport

client = skinport.Client()


@client.listen("saleFeed")
async def on_sale_feed(data):
    print(data)


@client.listen("maintenanceUpdated")
async def on_maintenance_updated(data):
    print(data)


@client.listen("steamStatusUpdated")
async def on_steam_status_updated(data):
    print(data)


client.run()
