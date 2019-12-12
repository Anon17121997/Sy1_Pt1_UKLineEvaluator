#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:26:08 2019

@author: thomasjhojlunddodd
"""
#https://pandapower.readthedocs.io/en/v1.4.1/networks/power_system_test_cases.html

#A more updated page was found:
#https://pandapower.readthedocs.io/en/v2.1.0/networks/power_system_test_cases.html

#Found a test case that represents the french high voltage scenario supposedly:
#Case 1888rte
#"This case accurately represents the size and complexity of French very high voltage and high voltage transmission network."

import pandapower.networks as pn

net = pn.case1888rte(ref_bus_idx=1246)