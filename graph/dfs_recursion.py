# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:06:01 2017

@author: zliu1
"""

def dfs(g,s,explore = False): # depth first search using recursion
    result = [s]
    if explore == False:
        explore = {}
        for e in list(g):
            explore[e] = -1
    explore[s] = 1
    for e in g[s]:
        if explore[e] == -1:
            explore[e] = 1
            result += dfs(g,e,explore)
    return result