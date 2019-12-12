#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:41:24 2019

@author: thomasjhojlunddodd
"""
print("The program started successfully")

import pandapower as pp
import numpy as np
import pandapower.networks as pn
import csv

net = pn.case1888rte(ref_bus_idx=1246)

x = range(0,200)#1975)
for i in x:
    try:
        net.line.at[i, 'r_ohm_per_km'] = 100
    
        pp.runpp(net)
    
        net.res_line.loc[net.res_line.loading_percent <= 100, 'equal_or_greater_than_100'] = 0
        net.res_line.loc[net.res_line.loading_percent > 100, 'equal_or_greater_than_100'] = 1
        failures = np.sum(net.res_line.equal_or_greater_than_100)
    
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([failures])
     
    except:    
        with open('/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["COCKUP"])
            
    net = pn.case1888rte(ref_bus_idx=1246)

print("Program finished successfully")