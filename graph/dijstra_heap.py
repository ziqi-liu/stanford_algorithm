# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:38:11 2017

@author: zliu1
"""

import os
import heapq
g = {}
os.chdir(r"C:\Users\zliu1\Desktop")
with open("dijkstraData.txt") as r:
    for line in r:
        l = line.split()
        g[int(l[0])] = []
        for e in l[1:]:
            f = e.split(",")
          
            g[int(l[0])].append({int(f[0]):int(f[1])})
print(g)
def shortest_path(g,s):
    v = {}
    add = s
    w = []
    for e in list(g):
        if e != s:
            w.append([1000000,e])
    heapq.heapify(w)
    v[s] = 0
    while w:
        #update
        for e in g[add]:
            for f in list(e):
                i = 0
                while i < len(w):
                    if w[i][1] == f and w[i][0] > v[add] + e[f]:
                        w[i] = w[-1]
                        w.pop()
                        if i < len(w):
                            heapq._siftup(w, i)
                            heapq._siftdown(w, 0, i)
                        heapq.heappush(w, [v[add] + e[f], f])
                    i += 1
        j = heapq.heappop(w)
        add = j[1]
        v[add] = j[0]
    return v

s = shortest_path(g,1)
print(s[7],s[37],s[59],s[82],s[99],s[115],s[133],s[165],s[188],s[197])
                    