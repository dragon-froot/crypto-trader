import json, time, requests

class CoinData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.url = "https://api.pro.coinbase.com"
    

    def order_book(self):
        response = requests.get('{0}/products/{1}/book'.format(self.url, self.symbol)).json()
        return response
    
    def day_stats(self):
        response = requests.get('{0}/products/{1}/stats'.format(self.url, self.symbol)).json()

        return response


    def historical_rates(self, dateRange):
        response = requests.get('{0}/products/{1}/candles'.format(self.url, self.symbol)).json()

        return r


symbol = "BTC-USD"
coin = CoinData(symbol)
historicalData = coin.historical_rates()

print(historicalData)







