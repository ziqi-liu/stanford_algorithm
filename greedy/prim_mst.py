# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 00:31:21 2017

@author: zliu1
"""

import os
import networkx
os.chdir(r"C:\users\zliu1\Desktop")
d = open("edges.txt").read().split()
d = [int(x) for x in d]
n = d.pop(0)
m = d.pop(0)
g = networkx.Graph()
i = 0
while i < m: 
    g.add_edge(d[3*i],d[3*i+1],weight = d[3*i+2])
    i +=1

x = [1]
t = []
while len(x) < n:
    m = float('inf')
    for e in g.edges():
        if g[e[0]][e[1]]['weight'] < m:
            if e[0] in x and e[1] not in x:
                v = e
                m =  g[e[0]][e[1]]['weight']
            if e[0] not in x and e[1] in x:
                v = (e[1],e[0])
                m =  g[e[0]][e[1]]['weight'] 
    x.append(v[1])
    t.append(v)
count = 0
for e in t:
    count += g[e[0]][e[1]]['weight']
print(count)

s= networkx.minimum_spanning_tree(g, weight='weight')
count1 = 0
i = 1
while i<=n:
    for e in s[i]:
        count1 += s[i][e]['weight']
    i +=1
print(count1/2)    
s[3][2]['weight']
g.edges()