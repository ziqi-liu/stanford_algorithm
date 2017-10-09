# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:38:11 2017

@author: zliu1
"""

import os
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
    w = {}
    v[s] = 0
    for e in list(g):
        if e != s:
            w[e] = 1000000
    while w:
        #update
        for e in g[add]:
            for f in list(e):
                if f in w:
                    w[f] = min(w[f], v[add] + e[f])
        add = min(w,key=w.get)
        v[add] = w[add]
        dict.pop(w,add)
    return v

s = shortest_path(g,1)
print(s[7],s[37],s[59],s[82],s[99],s[115],s[133],s[165],s[188],s[197])
                    