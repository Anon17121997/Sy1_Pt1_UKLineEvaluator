#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:26:29 2019

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

x = range(160, ((len(net.res_line.index))-1))     #1975 # 160-180 good tester
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

#============= ANALYSING CSV OF MODELS RUN (FINDING TOP WORST LINES)

data = pd.read_csv("/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv")

print(data)

print(data.nlargest(3, ['total_excess_load']))

#============= ANALYSING CSV MODELS RUN (FINDING SECOND AND THIRD WORST LINES)

print("Program finished successfully")
