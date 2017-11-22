# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:02:09 2017

@author: zliu1
"""

import os 
import numpy as np
os.chdir(r"C:\users\zliu1\Desktop")
e = []
with open("knapsack1.txt") as d:
    for line in d:
        e.append([int(x) for x in line.split()])
f = e.pop(0)
w = f[0]
n = f[1]
v = np.zeros((n+1,w+1),dtype = int)
for i in range(1,n+1):
    for j in range(1,w+1):
        if e[i-1][1] > j:
            v[i][j] = v[i-1][j]
        else:
            v[i][j] = max(v[i-1][j], v[i-1][j - e[i-1][1]]+ e[i-1][0])
print(v[n][w])
