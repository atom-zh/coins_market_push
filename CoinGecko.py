from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

lists = cg.get_coins_list()
for line in lists:
    print(line)

a = cg.get_price(ids='ethereum', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
print(a)