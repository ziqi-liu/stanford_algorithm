# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:05:17 2017

@author: zliu1
"""

import os
import networkx
os.chdir(r"C:\users\zliu1\Desktop")
d = open("g3.txt").read().split()
d = [int(x) for x in d]
n = d.pop(0)
m = d.pop(0)
g = networkx.Graph()
i = 0
while i < m: 
    g.add_edge(d[3*i],d[3*i+1],weight = d[3*i+2])
    i +=1
    
import numpy as np
A = np.full((n+1,n+1,n+1),1000000,dtype = int )

for i in range(1,n+1):
    A[i][i][0] = 0
for (i,j) in g.edges():
    A[i][j][0] = g[i][j]['weight']


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i][j][k] = min(A[i][j][k-1], A[i][k][k-1]+A[k][j][k-1])

negative = 0
for i in range(1,n+1):
    if A[i][i][n] < 0:
        negative = 1
        break
print(negative)
shortest = float('inf')
for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j:
            shortest = min(shortest, A[i][j][n])
print(shortest)
