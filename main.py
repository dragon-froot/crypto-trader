import time
from auth_client import CBAuth
from urls import *
import requests
from auth_credentials import PASSPHRASE, KEY, SECRET

auth = CBAuth(KEY, SECRET, PASSPHRASE)

def test_accounts():
    response = requests.get(account_url(), auth=auth).json()
    accID=''
    for i in response:
        if i['currency'] == "BTC":
            return i
            
    
    get_wallet(accID)



    

print(test_accounts())

