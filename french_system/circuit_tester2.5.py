#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:51:11 2019

@author: thomasjhojlunddodd
"""

print("The program started successfully")

import pandapower as pp
import numpy as np
import pandapower.networks as pn
import csv

net = pn.case1888rte(ref_bus_idx=1246)

with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Index Number", "Failures", "Total excess load"])

x = range(0, 5)#((len(net.res_line.index))-1))     #1975
for i in x:
    try:
        net.line.at[i, 'r_ohm_per_km'] = 100
    
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

print("Program finished successfully")