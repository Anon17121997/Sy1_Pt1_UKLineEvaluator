#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:13:13 2019

@author: thomasjhojlunddodd
"""

import pandapower.networks as pn
from pandapower.plotting.plotly import pf_res_plotly
import pandapower as pp
import pandas as pd

net = pn.GBreducednetwork()

i = 1
while i < (((len(net.line.index))-1)+1):
    net.line.at[i, 'name'] = i
    net.line.at[i, 'std_type'] = i
    i += 1

net.load.scaling = 1.08298391
net.gen.scaling = 1.08298391
net.sgen.scaling = 1.08298391

#pp.drop_lines(net, [36])
#pp.drop_lines(net, [37])

pp.runpp(net)

#net.res_line.loading_percent = 100

pf_res_plotly(net)