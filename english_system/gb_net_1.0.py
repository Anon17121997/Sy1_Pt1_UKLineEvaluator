#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:24:24 2019

@author: thomasjhojlunddodd
"""

import pandapower.networks as pn

#net = pn.GBreducednetwork()
#pp.runpp(net)

#x = range(0, ((len(net.line.index))-1))

#for i in x:
    #net.line.loc[net.line.name, 'name'] = i
    
    #net.line.loc[net.line.index > -1, 'name2'] = [i]


#net = pn.GBreducednetwork()
#pp.runpp(net)

#i = 1
#while i < (((len(net.line.index))-1)+1):
   # net.line.at[i, 'name'] = i
   # i += 1
    
#net.line.at['net.line.index[i]', 'name'] = 10

#net.line.set_value('net.line.index[5]', 'name', 10)


#net.line.at[5, 'name'] = 10

from pandapower.plotting.plotly import pf_res_plotly
import pandas as pd
import pandapower as pp

data = pd.read_csv("/Users/thomasjhojlunddodd/desktop/results.csv")

print("These are the top most disruptive lines(by amount excess):")
print(data.nlargest(3, ['total_excess_load']))

print("\nThese are the top most disruptive lines(by number of failures):")
print(data.nlargest(3, ['failures']))

#========Finding the actual numbers of these lines based off the enumerator we create later.
print("\n")

worst_1 = (data.nlargest(3, ['failures'])).iat[0,0]
worst_2 = (data.nlargest(3, ['failures'])).iat[1,0]
worst_3 = (data.nlargest(3, ['failures'])).iat[2,0]

print(f"Therefore, the most disruptive line, by number of failures, is the line of index number {worst_1}")
print(f"Whilst the second most disruptive is {worst_2}")
print(f"And the third most disruptive is {worst_3}")


net = pn.GBreducednetwork()

i = 1
while i < (((len(net.line.index))-1)+1):
    net.line.at[i, 'name'] = i
    net.line.at[i, 'std_type'] = i
    i += 1

pp.runpp(net)
pf_res_plotly(net)

