#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:52:58 2019

@author: thomasjhojlunddodd
"""

from OSGridConverter import latlong2grid
import pandapower.networks as pn

net = pn.case1888rte(ref_bus_idx=1246)

x = range(0, ((len(net.bus_geodata.index))-1))
for i in x:
    g = latlong2grid(net.bus_geodata.x[i], net.bus_geodata.y[i])
    
    net.bus_geodata.x[i] = g.E
    net.bus_geodata.y[i] = g.N


#g = latlong2grid(52.657977,1.716038)

#print(g.E, g.N)
    
print(net.bus_geodata)