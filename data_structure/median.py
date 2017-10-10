# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:49:23 2017

@author: zliu1
"""
import os
os.chdir(r"C:\users\zliu1\desktop")
l = open("median.txt").read().split()
l = [int(x) for x in l]

import heapq
a,b = [],[]

heapq.heappush(a,-l[0])
i = 1
result = [l[0]]
while i < len(l):
    if l[i] <= -a[0]:
        heapq.heappush(a,-l[i])
    else:
        heapq.heappush(b,l[i])
    if len(a) >= len(b) + 2:
        heapq.heappush(b,-heapq.heappop(a))
    elif len(a) < len(b):
        heapq.heappush(a,-heapq.heappop(b))
    result.append(-a[0])
    i += 1
sum(result) % 10000


