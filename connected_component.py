# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import queue

def cc(g): #calculate connected component for an undirected graph
    explore = {}
    result = []
    for e in list(g):
        explore[e] = -1
    for e in list(g):
        if explore[e] == -1:
            result.append(bfs(g,e,explore))
    return result
        


def bfs(g,s,explore): # breath first search 
    q = queue.Queue()
    result = []  
    q.put(s)
    explore[s] = 1
    while not q.empty():
        u = q.get()
        result.append(u)
        for e in g[u]:
            if explore[e] == -1:
                explore[e] = 1
                q.put(e)
                
    return result




