# import requests

# def get_bitcoin_price():
#     url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
#     response = requests.get(url)
        
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         price = data['bitcoin']['usd']
#         return price
#     else:
#         print("Error fetching data:", response.status_code)
#         return None
    
# if __name__ == '__main__':
#     price = get_bitcoin_price()
#     if price is not None:
#         print(f"The current price of Bitcoin is: ${price}")

from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.converter import BitcoinConverter

def get_bitcoin_to_usd():
    btc_converter = BitcoinConverter()
    price = btc_converter.get_latest_price('USD')
    return price

if __name__ == '__main__':
    price = get_bitcoin_to_usd()
    print(f"The current price of Bitcoin in USD is: ${price}")