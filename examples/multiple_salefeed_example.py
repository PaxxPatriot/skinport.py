import skinport
from skinport import AppID, Currency, Locale
client = skinport.Client()


@client.listen("saleFeed")
async def on_sale_feed(data):
    salefeed = skinport.SaleFeed(data=data)
    sales = salefeed.sales

    print(f"Event Type: {salefeed.event_type}")
    # For more attributes check out the documentation: https://paxxpatriot.github.io/skinport.py/api.html#skinport.SaleFeedSale
    print(f"Market Hash Names: {", ".join([sale.category_localized for sale in sales])}")


@client.listen("maintenanceUpdated")
async def on_maintenance_updated(data):
    print(data)


@client.listen("steamStatusUpdated")
async def on_steam_status_updated(data):
    print(data)


client.add_sale_feed(app_id=AppID.tf2)
client.add_sale_feed(currency=Currency.usd) # Default app_id is 730
client.add_sale_feed(currency=Currency.cny, locale=Locale.zh) # Default app_id is 730
client.run()
