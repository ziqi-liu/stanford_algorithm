# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import queue


def bfs(g,s): # breath first search with layers
    result = {}
    for e in list(g):
        result[e] = -1
    q = queue.Queue()
    q.put(s)
    result[s] = 0
    while not q.empty():
        u = q.get()
        for e in g[u]:
            if result[e] == -1:
                result[e] = result[u] + 1
                q.put(e)
    return result


    


