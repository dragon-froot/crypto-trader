# All of the urls that we are going to need

def account_url():
    return 'https://api.pro.coinbase.com/accounts'

def account_from_id_url(id):
    return 'https://api.pro.coinbase.com/accounts/{0}'.format(id)

# Post to this url to place order
def place_order():
    """
        {
            "size": "0.01",
            "price": "0.100",
            "side": "buy",
            "product_id": "BTC-USD"
        }
    """
    return 'https://api.pro.coinbase.com/orders'
