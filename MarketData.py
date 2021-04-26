import time, requests
from urls import *
from auth_client import CBAuth
from auth_credentials import PASSPHRASE, KEY, SECRET

class MarketData:
    def __init__(self):
        # self.currency = currency
        self.auth = CBAuth(KEY,SECRET,PASSPHRASE)
    

    def currencies(self):
        response = requests.get(get_currencies()).json()

        return response

    def products(self):
        response = requests.get(get_products()).json()

        return response
    

    def product_from_id(self, product_id):
        response = requests.get(get_product_by_id(product_id), auth=self.auth).json()

        return response
    
    def product_order_book(self, product_id, level):
        response = requests.get(get_product_order_book(product_id, level), auth=self.auth).json()

        return response

    def product_trades(self, product_id):
        response = requests.get(get_product_trades(product_id), auth=self.auth).json()

        return response
    
    def get_historic_rates(self, product_id, start, end, timeslice):
        url = get_historic_trades(product_id, start, end, timeslice)
        response = requests.get(url, auth=self.auth).json()

        return response

    def get_24hr_stats(self, product_id):
        response = requests.get(get_24hr_stats(product_id), auth=self.auth).json()

        return response