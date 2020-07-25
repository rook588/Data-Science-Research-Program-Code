# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

import sys

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360, retries = 1)

kw_list = ['Overwatch', 'Candy Crush']

pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')  

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


years = [2017, 2018, 2019]

"""

df = pytrends.get_historical_interest(kw_list, year_start = year, month_start = month, day_start = 1, hour_start = 0, year_end = year, month_end = month, day_end = 9, hour_end = 23, cat = 0, geo='', gprop = '', sleep = 0)
df.to_csv("pytrend_games_" + str(year) + "_" + str(month) + ".csv")
"""

for year in years:
    for month in range(1, 7):

        df = pytrends.get_historical_interest(kw_list, year_start = year, month_start = month, day_start = 1, hour_start = 0, year_end = year, month_end = month, day_end = days[month-1], hour_end = 23, cat = 0, geo='', gprop = '', sleep = 0)
        df.to_csv("pytrend_games_" + str(year) + "_" + str(month) + ".csv")
        df = pytrends.get_historical_interest(kw_list, year_start = year, month_start = month, day_start = 1, hour_start = 0, year_end = year, month_end = month, day_end = days[month-1], hour_end = 23, cat = 0, geo='', gprop = '', sleep = 0)
        df.to_csv("pytrend_games_" + str(year) + "_" + str(month) + ".csv")






  
  
    




