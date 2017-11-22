# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:02:09 2017

@author: zliu1
"""

import os 
import numpy as np
os.chdir(r"C:\users\zliu1\Desktop")
e = []
with open("knapsack_big.txt") as d:
    for line in d:
        e.append([int(x) for x in line.split()])
f = e.pop(0)
w = f[0]
n = f[1]
g = {}
import sys

iMaxStackSize = 5000
sys.setrecursionlimit(iMaxStackSize)
def knapsack(n,w):
    if n <= 0:
        return 0
    if w <= 0:
        return 0
    if (n,w) not in g:
        if e[n-1][1] > w:
            g[(n,w)] = knapsack(n-1,w)
        else:
            g[(n,w)] = max(knapsack(n-1,w),knapsack(n-1,w-e[n-1][1])+e[n-1][0])
    return g[(n,w)]
knapsack(n,w)
