import json, time, requests, hmac, hashlib, base64
from auth_credentials import (api_key, api_pass, api_secret)
from watchlist import watchlist
from requests.auth import AuthBase

class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
    
    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')


        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request
        

def test_auth():
    api_url = 'https://api.pro.coinbase.com/'
    auth = CoinbaseExchangeAuth(api_key, api_secret, api_pass)

    r = requests.get(api_url + 'accounts', auth=auth)
    print(r.json())

test_auth()










