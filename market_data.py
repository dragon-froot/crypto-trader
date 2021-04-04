import json, time, requests

class CoinData:
    def __init__(self, symbol):
        self.symbol = symbol
        self.url = "https://api.pro.coinbase.com"
    

    def get_market_data(self):
        response = requests.get('{0}/products/{1}/book'.format(self.url, self.symbol)).json()
        return response

    # Get historical data for a given time range
    def get_historical_data(self):
        pass




class Monitor:
    def __init__(self, symbol, timeout):
        self.symbol = symbol
        self.timeout = timeout
    # Make sure to provide a ticker and a timeout time
    def monitor_pricing(self):
        price = CoinData(self.symbol)

        print(price.get_market_data())
        time.sleep(self.timeout)

# This function will grab the a value every X ammount of time and store it 
def store_info(tp, currentCoinObj, previousCoinObj):
    timePeriod = tp



while True:
    Monitor("BTC-USD", 5).monitor_pricing()



