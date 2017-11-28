# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:05:17 2017

@author: zliu1
"""

import os
import networkx as nx
os.chdir(r"C:\users\zliu1\Desktop")
d = open("g1.txt").read().split()
d = [int(x) for x in d]
n = d.pop(0)
m = d.pop(0)
g = nx.DiGraph()
i = 0
while i < m: 
    g.add_edge(d[3*i],d[3*i+1],weight = d[3*i+2])
    i +=1

for i in range(1,n+1):
    g.add_edge(0,i,weight = 0)
import numpy as np
a = np.zeros((n+1,n+1),dtype=int)
for k in range(1,n+1):
    for i in range(1,n+1):
        a[i][k] = a[i][k-1]
        for u,v in g.in_edges(i):
            a[i][k] = min(a[i][k],a[u][k-1]+g[u][i]['weight'])
for i in range(1,n+1):
    if a[i][n] != a[i][n-1]:
        print('error detected!')
        break
#reweight

for u,v in g.edges():
    g[u][v]['weight'] = g[u][v]['weight'] + a[u][n] - a[v][n]
#dijkstra
length = nx.all_pairs_dijkstra_path_length(g,weight='weight')
#reconstruct
minimum = float('inf')
for i in range(1,n+1):
    for j in range(1,n+1):
        length[i][j] = length[i][j] + a[j][n] - a[i][n]
        minimum = min(minimum,length[i][j])
print(minimum)
