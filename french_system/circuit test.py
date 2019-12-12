#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:49:41 2019

@author: thomasjhojlunddodd
"""

#============= IMPORTING RELEVANT MODULES

print("The program started successfully")

import pandapower as pp
import numpy as np
import pandapower.networks as pn

#============= IMPORTING RELEVANT MODULES

net = pn.case1888rte(ref_bus_idx=1246)

sum_of_load_mw = (np.sum(net.load.p_mw))
sum_of_load_gw = (sum_of_load_mw/1000)

pp.runpp(net)

print(f"The sum total of installed load is {sum_of_load_mw} MW")
print(f"Or this can be expressed as {sum_of_load_gw} GW")

#============= IMPORTING RELEVANT MODULES

net = pn.case1888rte(ref_bus_idx=1246)

net.load.loc[:,'scaling'] = 1.5
net.gen.loc[:,'scaling'] = 1.5

net.load.scaling = 1.55
net.gen.scaling = 1.55

pp.runpp(net)

sum_of_load_mw_2 = ((net.load.p_mw).sum())
sum_of_load_gw_2 = (sum_of_load_mw_2/1000)
print(f"The sum total of installed load is {sum_of_load_mw_2} MW")
print(f"Or this can be expressed as {sum_of_load_gw_2} GW")

#=============


print("Program finished successfully")