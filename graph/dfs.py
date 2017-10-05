# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




import queue
def dfs(g,s): # depth first search 
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

    


