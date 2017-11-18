# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:29:34 2017

@author: zliu1
"""
import os
os.chdir(r"C:\users\zliu1\Desktop")
m = {}
e = []
with open("clustering_big.txt") as d:
    for line in d:
        e.append(line.split())

f = e.pop(0)
n = f[0]
k = f[1]

for i in e:
    t = ''
    for j in i:
        t = t + j
    m[t] = 0
    

def neibor(c):
    result = []
    for i in range(0,len(c)):
        if c[i] == '0':
            result.append(c[0:i] + '1' + c[ i+ 1:])
        else:
            result.append(c[0:i] + '0' + c[ i+ 1:])
    return list(set(result))

def neiborneibor(c):
    result = neibor(c)
    for i in neibor(c):
        result = result + neibor(i)
    return list(set(result)-set([c]))    

cl = {}
cluster = 1
for e in m:
        already = []
        for i in neiborneibor(e):
            if i in m and m[i] != 0 and m[i] not in already:
                already.append(m[i])
        if not already:
            if m[e] == 0:
                m[e] = cluster
                cl[cluster] = [e]
                for i in neiborneibor(e):
                    if i in m:
                        cl[cluster].append(i)
                        m[i] = cluster
                cluster += 1
        else:
           for i in already[1:]:
               for j in cl[i]:
                   cl[already[0]].append(j)
                   m[j] = already[0] 
               cl.pop(i)
           if m[e] == 0:
               m[e] = already[0]
               cl[already[0]].append(e)
               for i in neiborneibor(e):
                   if i in m:
                       m[i] = already[0]
                       cl[already[0]].append(i)
        
len(cl)
