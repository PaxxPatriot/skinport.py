import skinport

client = skinport.Client()


@client.event
async def on_sale_feed(data):
    print(data)


client.run()
