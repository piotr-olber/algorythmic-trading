#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:50:11 2024

@author: peter
"""
import numpy as np
import matplotlib.pyplot as plt
from trading_tools import get_data

class Strategy:
    
    def __init__(self, ticker_name):
        self.ticker_name = ticker_name
        self.data = get_data(ticker_name)
        self.__calculate_base_data()
    
    def __calculate_base_data(self):
        self.data['Returns'] = np.log(self.data.Close.div(self.data.Close.shift(1))) # Add daily return
        self.data['Position'] = 0
        self.data['Strategy'] = 0.00
        #self.data.dropna(inplace=True)
        
    def __calculate_return(self, data):
        ret = np.exp(data.sum())
        return round((ret - 1) * 100, 2)        
    
    def return_histogram(self):
        self.data.Returns.hist(bins=100, figsize=(12, 8))
        plt.title(f'{self.ticker_name} returns histogram')
        plt.show()
        
    def run(self):
        self.data['Position'] = 1
        self.data['Strategy'] = self.data.Position.shift(1) * self.data['Returns']
    
    def buy_and_hold_return(self):
        #ret = np.exp(self.data.Returns.sum())
        #return round((ret - 1) * 100, 2)
        return self.__calculate_return(self.data.Returns)
    
    def strategy_return(self):
        ret = np.exp(self.data.Strategy.sum())
        return round((ret - 1) * 100, 2)
        