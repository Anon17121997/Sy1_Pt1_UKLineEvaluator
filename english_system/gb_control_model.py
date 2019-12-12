#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:13:40 2019

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

net = pn.GBreducednetwork()

#============= CREATING CSV IN WHICH MODEL DATA IS INPUTTED

with open('/Users/thomasjhojlunddodd/desktop/results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["index_number", "failures", "total_excess_load"])

#============= RUNNING MODEL SIMULATIONS

x = range(0, ((len(net.res_line.index))-1))     #1975 # 160-180 good tester
for i in x:
    try:
        #net.load.scaling = 1.55
        #net.gen.scaling = 1.55
        #net.sgen.scaling = 1.55
        
        #pp.drop_lines(net, [i])
        

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
        
        with open('/Users/thomasjhojlunddodd/desktop/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([index_number2, failures2, sum_of_failure_excess])
            
    except:    
        with open('/Users/thomasjhojlunddodd/desktop/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([net.res_line.index[i], "N/A", "N/A"])   
        
    net = pn.GBreducednetwork()

#============= FILTERING END RESULTS
#https://www.rte-france.com/en/screen/europe-s-biggest-transmission-system
#Based on the fact that lines must be above 225000 to qualify as extra high voltage, 
#we must filter the results on the CSV.





#============= ANALYSING CSV OF MODELS RUN (FINDING TOP WORST LINES)

data = pd.read_csv("/Users/thomasjhojlunddodd/desktop/results.csv")

print(data)

print(data.nlargest(3, ['total_excess_load']))

#============= FINDING LOAD AT BASE MODEL

net = pn.case1888rte(ref_bus_idx=1246)

sum_of_load_mw = (np.sum(net.load.p_mw))
sum_of_load_gw = (sum_of_load_mw/1000)

pp.runpp(net)

print("Loads under base model:")
print(f"The sum total of installed load is {sum_of_load_mw} MW")
print(f"Or this can be expressed as {sum_of_load_gw} GW")

#============= FINDING LOAD AT PEAK TIME

sum_of_peakload_mw = sum_of_load_mw * 1.55
sum_of_peakload_gw = sum_of_load_gw * 1.55

print("Loads under altered model:")
print(f"The sum total of installed load is {sum_of_peakload_mw} MW")
print(f"Or this can be expressed as {sum_of_peakload_gw} GW")

#=============

print("Program finished successfully")