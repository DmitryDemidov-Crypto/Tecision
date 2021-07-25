# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 00:31:50 2021

@author: Asahi
"""

from binance.client import Client
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

Api_Key = ''
Api_Secret = ''

client = Client(Api_Key, Api_Secret)

def mdrn_plot(X_D, Y_D, dpi, hei, wid, color, type_p, x_l, y_l):
    
    plt.rcParams['savefig.facecolor'] = "0.9"  
    plt.rcParams['lines.linewidth'] = "4"
    plt.rcParams['axes.linewidth'] = "3" 
    plt.rcParams['axes.linewidth'] = "3" 
    plt.rcParams['ytick.major.width'] = "3" 
    plt.rcParams['xtick.major.width'] = "3" 
    plt.rcParams['ytick.major.size'] = "10" 
    plt.rcParams['xtick.major.size'] = "10" 
    plt.rcParams['legend.handlelength'] = "1.6" 
    plt.rcParams['legend.frameon'] = "False" 
    plt.rcParams['font.size'] = '22'
    
    
    rc = {"font.family" : "serif", "mathtext.fontset" : "stix"}
    
    plt.rcParams.update(rc)
    
    matplotlib.rcParams['mathtext.default'] = 'regular'
        
    fig, ax = plt.subplots(dpi = dpi) 
    fig.set_figheight(hei) ; fig.set_figwidth(wid)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel(x_l, fontsize = 30)
    ax.set_ylabel(y_l, fontsize = 30 )

    if type_p == 'plot':
        ax.plot(X_D,Y_D, color = color, linewidth= 1.7)
    
    if type_p == 'scatter':
        ax.scatter(X_D, Y_D, s = 160, color = color)

    plt.show()
    
    return 'plotted!'

def mdrn_hist(data, bins ,dpi, hei, wid, color, x_l, y_l):
    
    plt.rcParams['savefig.facecolor'] = "0.9"  
    plt.rcParams['lines.linewidth'] = "4"
    plt.rcParams['axes.linewidth'] = "3" 
    plt.rcParams['axes.linewidth'] = "3" 
    plt.rcParams['ytick.major.width'] = "3" 
    plt.rcParams['xtick.major.width'] = "3" 
    plt.rcParams['ytick.major.size'] = "10" 
    plt.rcParams['xtick.major.size'] = "10" 
    plt.rcParams['legend.handlelength'] = "1.6" 
    plt.rcParams['legend.frameon'] = "False" 
    plt.rcParams['font.size'] = '22'
    
    
    rc = {"font.family" : "serif", 
          "mathtext.fontset" : "stix"}
    
    plt.rcParams.update(rc)
    
    matplotlib.rcParams['mathtext.default'] = 'regular'
        
    fig, ax = plt.subplots(dpi = dpi) 
    fig.set_figheight(hei) ; fig.set_figwidth(wid)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel(x_l, fontsize = 30)
    ax.set_ylabel(y_l, fontsize = 30 )

    ax.hist(data, bins = bins, color = color)

    plt.show()
    
    return 'plotted!'

def MinMax_Scale(data_frame): 
    return (data_frame - data_frame.min()) / (data_frame.max() - data_frame.min())


def get_symbols(clnt, filt = 'none'):
    
    prices = clnt.get_all_tickers()
    all_symbols  = [obj['symbol'] for obj in prices]
    filt_symbols = all_symbols
    
    if not filt == 'none':
        
        filt_symbols = []
        
        for symb in all_symbols:
        
            c_name_l = len(filt)
            ver_l = 0
            
            for j_n in range(c_name_l):
                if symb[-1 - j_n] == filt[-1 - j_n]:
                    ver_l+=1
                    
            if ver_l == c_name_l:
                filt_symbols.append(symb)
                
    return filt_symbols


def get_symbol_trade_data(clnt, smbl, delta_t = 12000):

    now = clnt.get_server_time()['serverTime']
    past = now - delta_t

    trades = client.get_aggregate_trades(symbol = smbl, startTime = past, endTime  = now )
    
    output = {} ; len_cup = len(trades)
    
    if  len_cup > 0:
        
        frame = pd.DataFrame(trades)
        
        len_data = frame.shape[0]
        
        time_int_row =  pd.to_numeric(frame['T'])
        fit_dom = MinMax_Scale(time_int_row)
        
        frame['T']  = pd.to_datetime(frame['T']/1000, unit = 's')
        
        frame['p'] = pd.to_numeric(frame['p'])
        frame['q'] = pd.to_numeric(frame['q'])
        
        mean        =  frame['p'].mean()
        median      =  frame['p'].median()
        volatility  =  frame['p'].mad()
        
        if len_cup > 1:
            slope       =  np.polyfit(fit_dom, frame['p'], 1)[0]
        else:
            slope       =  0.0
        
        output.update({'mean' : mean, 'median' : median, 'volatility' : volatility, 'slope' : slope})
        
        open_p        =  frame['p'][0]
        close         =  frame['p'][len_data-1]
        high          =  frame['p'].max()
        low           =  frame['p'].min()
        
        volume        =  frame['q'].sum()
        
        output.update({'open_p' : open_p, 'close' : close, 'high' : high, 'low' : low})
        output.update({'volume' : volume})

        
    return output

print(get_symbol_trade_data(client, 'BTCUSDT'))
