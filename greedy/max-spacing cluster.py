# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:29:34 2017

@author: zliu1
"""
import os
os.chdir(r"C:\users\zliu1\Desktop")
m = []
with open("clustering1.txt") as d:
    for line in d:
        m.append([int(x) for x in line.split()])
n = m.pop(0)
print(m)
n = n[0]
for e in m:
    e[0],e[1],e[2] = e[2],e[0],e[1]
m.sort()
a = []
i = 0
while(i <= n):
    a.append(i)
    i += 1
count = n
while (count > 4):
    e = m.pop(0)
    if (a[e[1]] != a[e[2]]):
        p,q = a[e[1]],a[e[2]]
        count = count - 1
        i = 1
        while(i <= n):
            if(a[i] == p):
                a[i] = q
            i += 1
    
len(m)


while (True):
    e = m.pop(0)
    if (a[e[1]] != a[e[2]]):
        print([e[0])
        break

