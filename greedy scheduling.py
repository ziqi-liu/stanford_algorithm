# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:54:20 2017

@author: zliu1
"""

import os
os.chdir(r"C:\users\zliu1\Desktop")
d = open('jobs.txt').read().split()
d = [int(x) for x in d]
n = d.pop(0)
i,e = 1,[]
while i <= n:
    e.append([d[2*i-2],d[2*i-1]])
    i += 1
    
# greedy algorithm for scheduling
for i in e:
    i.append(i[0]/i[1])
    i[0],i[1],i[2] = i[2],i[0],i[1]
e.sort(reverse = True)
complete, result = 0,0
for i in e:
    complete += i[2]
    result += complete * i[1]
print(result)