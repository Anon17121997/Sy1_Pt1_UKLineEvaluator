#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:58:19 2019

@author: thomasjhojlunddodd
"""

print("The program started successfully")

import pandapower as pp
import numpy as np
import pandapower.networks as pn
import csv

net = pn.case1888rte(ref_bus_idx=1246)

x = range(0,20)#1975)
for i in x:
    try:
        #net.line.at[i, 'r_ohm_per_km'] = 100
        pp.drop_lines(net, lines = [i])
    
        pp.runpp(net)
    
        net.res_line.loc[net.res_line.loading_percent <= 100, 'equal_or_greater_than_100'] = 0
        net.res_line.loc[net.res_line.loading_percent > 100, 'equal_or_greater_than_100'] = 1
        #-----
        net.res_line.loc[net.res_line.loading_percent > 100, 'excess_over_100'] = (net.res_line.loading_percent - 100) #
        net.res_line.loc[net.res_line.loading_percent <= 100, 'excess_over_100'] = 0 #
        #-----
        sum_of_failure_excess = np.sum(net.res_line.excess_over_100) #
        failures = np.sum(net.res_line.equal_or_greater_than_100)
    
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([failures])
            
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results2.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sum_of_failure_excess])
     
    except:    
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["COCKUP"])
            
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results2.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["COCKUP"])            
        
    net = pn.case1888rte(ref_bus_idx=1246)

print("Program finished successfully")