import json,os
from web3 import Web3
import krakenex
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv

class CoinGeckoAPI():
    def __init__(self, API_KEY_COIN_GECKO):
        self.API_KEY_COIN_GECKO = API_KEY_COIN_GECKO
  
    def get_token_id(self,name):
        url = f"https://api.coingecko.com/api/v3/search?query={name}"
        response = requests.get(url)
        data = response.json()
        if data and 'coins' in data and data['coins']:
            return data['coins'][0]['id']
        else:
            return None

    def get_token_price(self,name):
     
        token_id=self.get_token_id(name)
        crc = "usd"
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies={crc}&x_cg_demo_api_key={self.API_KEY_COIN_GECKO}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if token_id in data:
                return data[token_id]['usd']
            else:
                return None
        else:
            print('Error:', response.status_code)
            return None