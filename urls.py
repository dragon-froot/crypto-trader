# All of the urls that we are going to need

def account_url():
    return 'https://api.pro.coinbase.com/accounts'

def account_from_id_url(account_id):
    return 'https://api.pro.coinbase.com/accounts/{0}'.format(account_id)

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

def cancel_order(order_id):
    # Take the ID from the order above and post here
    return 'https://api.pro.coinbase.com/orders/{}'.format(order_id)

# This function will return all fo the orders
def get_orders():
    return 'https://api.pro.coinbase.com/orders'

def get_transfers():
    return 'https://api.pro.coinbase.com/transfers'

def get_currencies():
    return 'https://api.pro.coinbase.com/currencies'

def get_products():
    return 'https://api.pro.coinbase.com/products'

def get_product_by_id(product_id):
    return 'https://api.pro.coinbase.com/product/{0}'.format(product_id)