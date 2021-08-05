# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:40:46 2021

@author: HP
"""

import pandas as pd
import os
my_path = os.path.abspath(__file__) # Figures out the absolute path for you in case your working directory moves around.


def quantity_line():
    table = pd.read_csv('E:/Spyder projects/Expense/expense.txt')
    table = table.quantity.plot.line().get_figure()
    table.savefig('quanitiy_line_plot.png')