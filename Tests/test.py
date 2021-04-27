from MarketData import MarketData
from CoinAccount import Account
from auth_clientu import CBAuth
from auth_credentials import PASSPHRASE, KEY, SECRET
from urls import *

class Test(MarketData):
    def __init__(self):
        self.product_id = 'BTC'
        self.marketDataFunctionList = list(
                self.currencies(),
                self.products(),
                self.product_from_id(self.product_id),
                self.product_order_book(self.product_id, 3),
                self.product_trades(self.product_id),
                self.get_historic_rates(self.product_id),
                self.get_24hr_stats(self.product_id)
            )
        self.auth = CBAuth(KEY, SECRET, PASSPHRASE)accountData = Account()
    
    def test_market_data_functions(self):
        pass
