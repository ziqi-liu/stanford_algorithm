# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:27:41 2017

@author: zliu1
"""

import os
os.chdir(r'C:\users\zliu1\desktop')
l = open('2sum.txt').read().split()
l = [int(x) for x in l]
l.sort()
h = {}
for e in l:
    if e not in h:
        h[e] = 1
    else:
        h[e] += 1
count = 0
for e in list(h):
    if h[e] > 1:
        h.pop(e)
g = {}
for e in list(h):
    if e // 10000 in g:
        g[e // 10000].append(e)
    else:
        g[e // 10000] = [e]
result = []
for e in h:
    if (- e // 10000 - 1)  in g:
        for f in g[- e // 10000 - 1]:
            if -10000 <= e + f <= 10000 and f!= e and e + f not in result:
                result.append(e + f)
    if (- e // 10000)  in g:
        for f in g[- e // 10000]:
            if -10000 <= e + f <= 10000 and f!= e and e + f not in result:
                result.append(e + f)
    if (- e // 10000 + 1)  in g:
        for f in g[- e // 10000 + 1]:
            if -10000 <= e + f <= 10000 and f!= e and e + f not in result:
                result.append(e + f)

len(result)
