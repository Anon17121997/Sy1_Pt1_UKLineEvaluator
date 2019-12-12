#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:46:00 2019

@author: thomasjhojlunddodd
"""

import pandas as pd

data = pd.read_csv("/Users/thomasjhojlunddodd/documents/lpthw/Sy1/power_plants/results.csv")
#data.head()

max_excess_load = data['Failures'].max()
print(max_excess_load)