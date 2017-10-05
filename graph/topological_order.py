# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:06:01 2017

@author: zliu1
"""

def topological_sort(g): #compute the topological order for a directed graph
    explore = {}
    result = {}
    for e in list(g):
        explore[e] = -1
    for e in list(g):
        if explore[e] == -1:
            dfs(g,e,result,explore)
    return result
    
def dfs(g,s,result,explore = False): 
    global score
    if explore == False:
        explore = {}
        for e in list(g):
            explore[e] = -1
    explore[s] = 1
    for e in g[s]:
        if explore[e] == -1:
            dfs(g,e,result,explore)
    result[s] = score
    score = score - 1
            



