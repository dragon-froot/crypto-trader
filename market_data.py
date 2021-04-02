import json, time, requests

class CoinData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.url = "https://api.pro.coinbase.com"
    

    def get_market_data(self):
        response = requests.get('{0}/products/{1}/book'.format(self.url, self.symbol)).json()
        return response



# Make sure to provide a ticker and a timeout time
def monitor_pricing(symbol, timeout):
    price = CoinData(symbol)

    print(price.get_market_data())
    time.sleep(timeout)


while True:
    monitor_pricing("BTC-USD", 5)



