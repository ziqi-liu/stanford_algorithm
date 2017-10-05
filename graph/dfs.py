# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os

g = {}
os.chdir(r'C:\users\zliu1\Desktop')
with open('kargerMinCut.txt') as f:
    for line in f:
        l= line.split()
        l = [int(x) for x in l]
        g[l[0]] = l[1:]


import queue
def dfs(g,s): # breath first search with layers
    explore = {}
    result = []
    for e in list(g):
        explore[e] = -1
    explore[s] = 1
    q = queue.LifoQueue()
    q.put(s)
    while not q.empty():
        u = q.get()
        result.append(u)
        for e in g[u]:
            if explore[e] == -1:
                explore[e] = 1
                q.put(e)
    return result

print(dfs(g,1))
    


