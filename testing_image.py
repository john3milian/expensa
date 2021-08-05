# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:43:13 2021

@author: HP
"""

import pandas as pd

table = pd.read_csv('expense.txt')
frequency = table.date.value_counts()
label = frequency.index.tolist()
y_data = frequency.tolist()