# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import os
import copy
g = {}
with open('kargerMinCut.txt') as f:
    for line in f:
        l= line.split()
        l = [int(x) for x in l]
        g[l[0]] = l[1:]
def mincut(g): #g={1:[],2:[],3:[]...} calculate the mincut for a graph in O(mn)
    if len(g) == 2:
        count = 0
        for e in g:
            count += len(g[e])
        return count/2
    u = random.choice(list(g))
    v = random.choice(g[u])
    for e in g:
        count = 0
        for f in g[e]:
            if f == v:
                count += 1
        g[e] = [x for x in g[e] if x!=v] + count * [u]
    g[u] += g[v]
    g.pop(v)
    g[u] = [x for x in g[u] if x!=u]
    return mincut(g)
os.chdir(r'C:\users\zliu1\Desktop')
i,m = 0,1000
while i < 100:
    f = copy.copy(g)
    m = min(m,mincut(f))
    i += 1
print(m)


