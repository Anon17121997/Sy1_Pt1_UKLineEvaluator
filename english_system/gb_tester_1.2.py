#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:04:12 2019

@author: thomasjhojlunddodd
"""

print("The program started successfully")

#============= IMPORTING RELEVANT MODULES

import pandapower as pp
import numpy as np
import pandapower.networks as pn
import csv
import pandas as pd
from pandapower.plotting.plotly import pf_res_plotly

#============= IMPORTING RELEVANT NETWORK MODEL

net = pn.GBreducednetwork()

#============= FINDING LOAD AT BASE MODEL

net = pn.GBreducednetwork()

sum_of_load_mw = (np.sum(net.load.p_mw))
sum_of_load_gw = (sum_of_load_mw/1000)

pp.runpp(net)

print("Loads under base model:")
print(f"The sum total of installed load is {sum_of_load_mw} MW")
print(f"Or this can be expressed as {sum_of_load_gw} GW\n")

#============= FINDING LOAD AT PEAK TIME

sum_of_peakload_mw = sum_of_load_mw * 1.08298391
sum_of_peakload_gw = sum_of_load_gw * 1.08298391

print("Loads under worst case scenario model:")
print(f"The sum total of installed load is {sum_of_peakload_mw} MW")
print(f"Or this can be expressed as {sum_of_peakload_gw} GW\n")

#============= CREATING CSV IN WHICH MODEL DATA IS INPUTTED

with open('/Users/thomasjhojlunddodd/desktop/results.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["index_number", "failures", "total_excess_load"])

#============= RUNNING MODEL SIMULATIONS

x = range(0, ((len(net.res_line.index))-1))
for i in x:
    try:
        net.load.scaling = 1.08298391
        net.gen.scaling = 1.08298391
        net.sgen.scaling = 1.08298391
        
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
        
        with open('/Users/thomasjhojlunddodd/desktop/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([index_number2, failures2, sum_of_failure_excess])
            
    except:    
        with open('/Users/thomasjhojlunddodd/desktop/results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([net.res_line.index[i], "N/A", "N/A"])   
        
    net = pn.GBreducednetwork()

#============= ANALYSING CSV OF MODELS RUN (FINDING TOP WORST LINES)

data = pd.read_csv("/Users/thomasjhojlunddodd/desktop/results.csv")

print("These are the top most disruptive lines(by amount excess):")
print(data.nlargest(3, ['total_excess_load']))

print("\nThese are the top most disruptive lines(by number of failures):")
print(data.nlargest(3, ['failures']))

worst_1 = (data.nlargest(3, ['failures'])).iat[0,0]
worst_2 = (data.nlargest(3, ['failures'])).iat[1,0]
worst_3 = (data.nlargest(3, ['failures'])).iat[2,0]

print(f"Therefore, the most disruptive line, by number of failures, is the line of index number {worst_1}")
print(f"Whilst the second most disruptive is {worst_2}")
print(f"And the third most disruptive is {worst_3}")

#============= PRINTING MAP OF LINES WITH NAMES

net = pn.GBreducednetwork()

i = 1
while i < (((len(net.line.index))-1)+1):
    net.line.at[i, 'name'] = i
    net.line.at[i, 'std_type'] = i
    i += 1

pp.runpp(net)
pf_res_plotly(net)

#=============

print("Program finished successfully")