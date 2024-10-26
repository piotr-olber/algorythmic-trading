#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:18:22 2024

@author: peter
"""
import numpy as np
import yfinance as yf

def get_data(symbol: str):
    data = yf.download(tickers=symbol, period='1y', interval='1d')
    data.reset_index(inplace=True, drop=True)
    return data

def calculate_return(data):
    data['Returns'] = np.log(data.Close.div(data.Close.shift(1))) # Add daily return
    data.dropna(inplace=True)
    return data