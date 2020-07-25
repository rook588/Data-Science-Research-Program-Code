#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:05:08 2020

@author: richard
"""


import csv

# fyear = 2017
# fmonth = 1

fyears = [2020]
fmonths = [1, 2, 3, 4, 5, 6, 7]

for fyear in fyears:
    for fmonth in fmonths:
        infile_name = f'pytrend_games_{fyear}_{fmonth}.csv'
        
        comp_dict = {}
        stock_dict = {}
        
        with open(infile_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                date_col = row['date']
                comp_score = row['Overwatch']
                stock_score = row['Candy Crush']
                
                
                if date_col in comp_dict:
                    comp_dict[date_col] = max(comp_dict[date_col], comp_score)
                    stock_dict[date_col] = max(stock_dict[date_col], stock_score)
                else:
                    comp_dict[date_col] = comp_score
                    stock_dict[date_col] = stock_score
                    

                
        
        outfile_name = f'pytrend_products_{fyear}_{fmonth}.csv'
        
        with open(outfile_name, mode='w') as result_file:
            fieldnames = ['date', 'Overwatch', 'Candy Crush']
            csv_writer = csv.DictWriter(result_file, fieldnames)
            csv_writer.writeheader()
            
            for d in comp_dict.keys():
                csv_writer.writerow({'date': d, 'Overwatch': comp_dict[d], 'Candy Crush': stock_dict[d]})
                
