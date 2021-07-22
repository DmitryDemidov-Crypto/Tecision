# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:17:14 2021

@author: Asahi
"""

from binance.client import Client



def buy_coin(coin_tag, volume, client_in_f, Type = 'Market', prc = 0.0):
    
    if Type == 'Limit':
        order = client_in_f.order_limit_buy(symbol= coin_tag, quantity= volume, price= str(prc))
    elif Type == 'Market':
        order = client_in_f.order_market_buy(symbol= coin_tag, quantity= volume)
    else:
        print('Incorrect order Type')
        
    return order


def sell_coin(coin_tag, volume, client_in_f, Type = 'Market', prc = 0.0):
    
    if Type == 'Limit':
        order = client_in_f.order_limit_sell(symbol= coin_tag, quantity= volume, price= str(prc))
    elif Type == 'Market':
        order = client_in_f.order_market_sell(symbol= coin_tag, quantity= volume)
    else:
        print('Incorrect order Type')
        
    return order
