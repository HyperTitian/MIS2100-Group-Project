# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:12:12 2021

@author: hands
"""

import pandas_datareader as reader
from datetime import date

def moving_average(ticker):
    
    today = date.today()
    Data = reader.DataReader(ticker, start = "2020-1-1", end = today, data_source = "yahoo")
    long_rolling = Data.Close.rolling(100).mean()
    return long_rolling.tail(5)