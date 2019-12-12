#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:07:11 2019

@author: thomasjhojlunddodd
"""

print("The program started successfully")

import pandapower as pp
import pandas as pd
import numpy as np
import pandapower.networks as pn
import csv
import sys

net = pn.case1888rte(ref_bus_idx=1246)

max_r = net.line['r_ohm_per_km'].max()
print(f"The max resistance per km is {max_r} ohms.")

user_input1 = input("What resistance would you like to run the model at? \n>>> ")
user_input2 = input("And what range of the indexed lines would you like to test? \nAll of them (ALL)\nFirst five of them (FIVE)\n>>> ")

if user_input2 == "ALL":
    synthesised_input2 = ((len(net.res_line.index))-1)
elif user_input2 == "FIVE":
    synthesised_input2 = 5
else:
    print("Invalid value")
    sys.exit()
    
with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Index Number", "Failures", "Total excess load"])

x = range(0, synthesised_input2)#((len(net.res_line.index))-1))     #1975
for i in x:
    try:
        net.line.at[i, 'r_ohm_per_km'] = user_input1
    
        pp.runpp(net)
    
        net.res_line.loc[net.res_line.loading_percent <= 100, 'equal_or_greater_than_100'] = 0
        net.res_line.loc[net.res_line.loading_percent > 100, 'equal_or_greater_than_100'] = 1
        #-----
        net.res_line.loc[net.res_line.loading_percent > 100, 'excess_over_100'] = (net.res_line.loading_percent - 100)
        net.res_line.loc[net.res_line.loading_percent <= 100, 'excess_over_100'] = 0
        #-----
        failures = np.sum(net.res_line.equal_or_greater_than_100)
        sum_of_failure_excess = np.sum(net.res_line.excess_over_100)
        index_number = net.res_line.index[i]
        
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([index_number, failures, sum_of_failure_excess])
            
    except:    
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([net.res_line.index[i], "N/A", "N/A"])   
        
    net = pn.case1888rte(ref_bus_idx=1246)
    
#HANDLING THE DATA PRODUCED (NOT FINISHED)
    
data = pd.read_csv("/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv")
data.head()

#HANDLING THE DATA PRODUCED
    
print("Program finished successfully")
    