#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:14:30 2019

@author: thomasjhojlunddodd
"""

print("The program started successfully")

#============= IMPORTING RELEVANT MODULES

import pandapower as pp
import numpy as np
import pandapower.networks as pn
import csv
import pandas as pd

#============= IMPORTING RELEVANT NETWORK MODEL

net = pn.case1888rte(ref_bus_idx=1246)

#============= CREATING CSV IN WHICH MODEL DATA IS INPUTTED

with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["index_number", "failures", "total_excess_load"])

#============= RUNNING MODEL SIMULATIONS

x = range(160, 180)  #((len(net.res_line.index))-1))     #1975
for i in x:
    try:
        pp.drop_lines(net, [i])
        
        pp.runpp(net)
        
        net.res_line.loc[net.res_line.loading_percent <= 100, 'equal_or_greater_than_100'] = 0
        net.res_line.loc[net.res_line.loading_percent > 100, 'equal_or_greater_than_100'] = 1
        #-----
        net.res_line.loc[net.res_line.loading_percent > 100, 'excess_over_100'] = (net.res_line.loading_percent - 100)
        net.res_line.loc[net.res_line.loading_percent <= 100, 'excess_over_100'] = 0
        #-----
        failures2 = np.sum(net.res_line.equal_or_greater_than_100)
        sum_of_failure_excess = np.sum(net.res_line.excess_over_100)
        index_number2 = net.res_line.index[i]
        
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([index_number2, failures2, sum_of_failure_excess])
            
    except:    
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([net.res_line.index[i], "N/A", "N/A"])   
        
    net = pn.case1888rte(ref_bus_idx=1246)

#============= ANALYSING CSV OF MODELS RUN (FINDING WORST LINE)
    
data = pd.read_csv("/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv")

print("\nFor the most vulnerable line:\n--------------")

max_number_failures = data['failures'].max()
print(f"The number of failures were: {max_number_failures}")

max_excess_load = data['total_excess_load'].max()
print(f"The failing lines were overloaded by a cumulative: {max_excess_load}%")

real_index_number = data.loc[data.total_excess_load == max_excess_load,'index_number'].tolist()
print(f"The line that was overloaded the most was indexed as (in reality): {real_index_number}")

index_max_load = (data['total_excess_load'].idxmax())+2
print(f"The line that was overloaded the most was indexed as (in CSV): {index_max_load} \n-------------")

#============= ANALYSING CSV MODELS RUN (FINDING SECOND AND THIRD WORST LINES)

print(data.nlargest(3, ['total_excess_load']))

print("Program finished successfully")