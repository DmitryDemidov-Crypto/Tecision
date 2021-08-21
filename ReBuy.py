# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 09:21:39 2021

@author: Asahi
"""

# ------------ Эта функция начинает работать, только если уже активен один из стоплоссов
#              иначе просто кнопка не нажимается

def rebuy_coins(input_price, coin, rebuy_percent, volume_percent):
    
    
    stoploss_status = get_stopstoploss_status()т            # Проверяем, сработал стоплосс или еще нет
    
    if stoploss_status == 'Not active':
        
        sell_price_from_stoploss = get_stoploss_sellprice() # Получаем цену, по которой продали монету coin
        stop_loss_volume = get_stoploss_sellvolume()        # Получаем количество стейблкоинов, 
                                                            # которые выручили с продажи по stoploss 
        
        
        if input_price <= sell_price_from_stoploss - sell_price_from_stoploss*rebuy_percent:
            
            buy_s_volume = stop_loss_volume*volume_percent  # Объём стейблкоинов для покупки равен проценту, который поставил
                                                            # пользователь в таблице, умноженный на stop_loss_volume
                                                          
            coin_volume =  buy_s_volume/input_price 
                                        
            # И вызываем тут просто функцию купить coin_volume этих монет и возвращаем статус ордера
            
            
            
            
            

            
            
            
            