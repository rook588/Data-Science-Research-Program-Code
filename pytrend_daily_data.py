#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:57:29 2020

@author: richard
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:05:08 2020

@author: richard
"""


import csv

# fyear = 2017
# fmonth = 1

fyears = [2017, 2018, 2019]
fmonths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
count = 0
blizzard_sum = 0
atvi_sum = 0
blizzard_median_temp = []
atvi_median_temp = []

blizzard_mean = {}
blizzard_median = {}
atvi_mean = {}
atvi_median = {}

diff1 = {}
diff2 = {}
diff3 = {}
diff4 = {}

blizzard_mean_prev = 0
blizzard_median_prev = 0
atvi_mean_prev = 0
atvi_median_prev = 0


date_actual = ""

for fyear in fyears:
    for fmonth in fmonths:
        infile_name = f'pytrend_products_{fyear}_{fmonth}.csv'
        #comp_dict = {}
        #stock_dict = {}
        
        with open(infile_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                date_col = row['date']
                date_actual = date_col[0:10]
                comp_score = row['Overwatch']
                stock_score = row['Candy Crush']
                blizzard_sum += int(comp_score)
                atvi_sum += int(stock_score)
                blizzard_median_temp.append(comp_score)
                atvi_median_temp.append(stock_score)
                count += 1;
                
                """
                if date_col in comp_dict:
                    comp_dict[date_col] = max(comp_dict[date_col], comp_score)
                else:
                    comp_dict[date_col] = comp_score
                
                if date_col in stock_dict:
                    stock_dict[date_col] = max(stock_dict[date_col], stock_score)
                else:
                    stock_dict[date_col] = stock_score
                """
                if (count % 24) == 0:
                    print(date_actual)
                    blizzard_median_temp.sort()
                    atvi_median_temp.sort()
                
                    blizzard_mean[date_actual] = blizzard_sum / 24.0
                    atvi_mean[date_actual] = atvi_sum / 24.0
                    blizzard_median[date_actual] = (int(blizzard_median_temp[11]) + int(blizzard_median_temp[12]))/2.0
                    atvi_median[date_actual] = (int(atvi_median_temp[11]) + int(atvi_median_temp[12]))/2.0
                    
                    if date_actual == "2017-01-01":
                        diff1[date_actual] = 0
                        diff2[date_actual] = 0
                        diff3[date_actual] = 0
                        diff4[date_actual] = 0
                        
                    else:
                        diff1[date_actual] = blizzard_mean[date_actual] - blizzard_mean_prev
                        diff2[date_actual] = blizzard_median[date_actual] - blizzard_median_prev
                        diff3[date_actual] = atvi_mean[date_actual] - atvi_mean_prev
                        diff4[date_actual] = atvi_median[date_actual] - atvi_median_prev
                        
                    blizzard_mean_prev = blizzard_mean[date_actual]
                    blizzard_median_prev = blizzard_median[date_actual]
                    atvi_mean_prev = atvi_mean[date_actual]
                    atvi_median_prev = atvi_median[date_actual]
                
                    blizzard_sum = 0
                    atvi_sum = 0
                    blizzard_median_temp = []
                    atvi_median_temp = []

fyears = [2020]
fmonths = [1, 2, 3, 4, 5, 6, 7]

for fyear in fyears:
    for fmonth in fmonths:
        infile_name = f'pytrend_products_{fyear}_{fmonth}.csv'
        #comp_dict = {}
        #stock_dict = {}
        
        with open(infile_name) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                date_col = row['date']
                date_actual = date_col[0:10]
                comp_score = row['Overwatch']
                stock_score = row['Candy Crush']
                blizzard_sum += int(comp_score)
                atvi_sum += int(stock_score)
                blizzard_median_temp.append(comp_score)
                atvi_median_temp.append(stock_score)
                
                    
                count += 1;
                """
                if date_col in comp_dict:
                    comp_dict[date_col] = max(comp_dict[date_col], comp_score)
                else:
                    comp_dict[date_col] = comp_score
                
                if date_col in stock_dict:
                    stock_dict[date_col] = max(stock_dict[date_col], stock_score)
                else:
                    stock_dict[date_col] = stock_score
                """
                if (count % 24) == 0:
                    #print(date_actual)
                    blizzard_median_temp.sort()
                    atvi_median_temp.sort()
                
                    blizzard_mean[date_actual] = blizzard_sum / 24.0
                    atvi_mean[date_actual] = atvi_sum / 24.0
                    blizzard_median[date_actual] = (int(blizzard_median_temp[11]) + int(blizzard_median_temp[12]))/2.0
                    atvi_median[date_actual] = (int(atvi_median_temp[11]) + int(atvi_median_temp[12]))/2.0
                    
                    if date_actual == "2017-01-01":
                        diff1[date_actual] = 0
                        diff2[date_actual] = 0
                        diff3[date_actual] = 0
                        diff4[date_actual] = 0
                        
                    else:
                        diff1[date_actual] = blizzard_mean[date_actual] - blizzard_mean_prev
                        diff2[date_actual] = blizzard_median[date_actual] - blizzard_median_prev
                        diff3[date_actual] = atvi_mean[date_actual] - atvi_mean_prev
                        diff4[date_actual] = atvi_median[date_actual] - atvi_median_prev
                        
                    blizzard_mean_prev = blizzard_mean[date_actual]
                    blizzard_median_prev = blizzard_median[date_actual]
                    atvi_mean_prev = atvi_mean[date_actual]
                    atvi_median_prev = atvi_median[date_actual]
                
                    blizzard_sum = 0
                    atvi_sum = 0
                    blizzard_median_temp = []
                    atvi_median_temp = []
        
outfile_name = "pytrend_daily_mean_median_data_games.csv"
        
with open(outfile_name, mode='w') as result_file:
    fieldnames = ['date', 'Overwatch Mean', 'Overwatch Mean Difference', 'Overwatch Median', 'Overwatch Median Difference', 'Candy Crush Mean', 'Candy Crush Mean Difference', 'Candy Crush Median', 'Candy Crush Median Difference']
    csv_writer = csv.DictWriter(result_file, fieldnames)
    csv_writer.writeheader()
            
    for d in blizzard_mean.keys():
        csv_writer.writerow({'date': d, 'Overwatch Mean': blizzard_mean[d], 'Overwatch Mean Difference': diff1[d], 'Overwatch Median': blizzard_median[d], 'Overwatch Median Difference': diff2[d], 'Candy Crush Mean': atvi_mean[d], 'Candy Crush Mean Difference': diff3[d], 'Candy Crush Median': atvi_median[d], 'Candy Crush Median Difference': diff4[d]})
