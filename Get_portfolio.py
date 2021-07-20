# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 00:00:12 2021

@author: Dmitry
"""

from binance.client import Client

Api_Key =    'jkkewu8EVwg2sDLX1Ousx2d2LIYi42doOqHwLE8LH2do1csi2BY1ulIDLAgPoIrd'
Api_Secret = 'ua7FSF1pzdflnWIS4TWrqnU1okMYCO643cyKM4zprsIOibq63r8bBxmKVHXGNKvx'

client = Client(Api_Key, Api_Secret)

Not_Crypto =   ['USD', 'RUB', 'Euro']

Stable_coins = ['USDT', 'USDC', 'BUSD', 'DAI', 'UST',
                'TUSD', 'PAX', 'HUSD', 'USDN', 'GUSD']

def Get_User_Portfolio(User_client, STABLE_C = 'USDT'):
    
    try:
        acc_info = User_client.get_account()
    except:
        print('Problems with getting accaunt info')
        return {}
    
    Wallet_Data = {'Global' :{}, 'Coins': {}}
    
    BTC_PRICE = float(User_client.get_avg_price(symbol = 'BTCUSDT')['price'])
    
    Total_USD = 0.0
    
    for coin_b in acc_info['balances']:
        if not float(coin_b['free']) == 0.0:
            
            Coin_n = coin_b['asset']
            Coin_w = float(coin_b['free'])
            
            if Coin_n == STABLE_C:
                Wallet_Data['Coins'].update({Coin_n : [Coin_w, Coin_w]})
                Total_USD += Coin_w
    
            if not Coin_n == STABLE_C and Coin_n in Stable_coins:
                Wallet_Data['Coins'].update({Coin_n : [Coin_w, Coin_w]})
                Total_USD += Coin_w
                
            if not Coin_n in Not_Crypto + Stable_coins:
            
                Pair_s = Coin_n + STABLE_C
                
                try:
                    Coin_p = float(User_client.get_avg_price(symbol = Pair_s)['price'])
                except:
                    print('Probably ' + Pair_s + ' is stable coin')
                    return {}
                
                Wallet_Data['Coins'].update({Coin_n : []})
                Wallet_Data['Coins'][Coin_n].extend([Coin_w, Coin_w*Coin_p])
                
                Total_USD += Coin_w*Coin_p
                
        Wallet_Data['Global'].update({'Total_in_USD': Total_USD, 'Total_in_BTC': Total_USD/BTC_PRICE})
            

    return Wallet_Data
    
print(Get_User_Portfolio(client))