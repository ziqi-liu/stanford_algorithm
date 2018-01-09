# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:08:14 2018

@author: zliu1
"""

import os
os.chdir(r"C:/users/zliu1/Desktop")
import numpy as np
d = open('tsp.txt').read().split()
d = [float(x) for x in d]
n = int(d.pop(0))
point = np.zeros((n,2),dtype = 'float')
for i in range(0,n):
    point[i][0] = d[2*i]
    point[i][1] = d[2*i+1]

def dis(x,y):
    return np.sqrt(pow(x[0]-y[0],2) + pow(x[1]-y[1],2))

def count1(a):
    result =0
    b = bin(a)[2:]
    for i in range(0,len(b)):
        if b[i] == '1':
            result +=1
    return result

def tsp(n,point):
    a = {}
    a[(pow(2,n-1),0)] = 0
    for m in range(2,n+1):
        for i in range(1,pow(2,n)):
            if count1(i) == m:
                for j in range(1,n):
                    x = bin(i)[2:]
                    x = (n-len(x))*'0'+x
                    if x[j] == '1':
                        mini = float('inf')
                        for k in range(0,n):
                            if (i-pow(2,n-j-1),k) in a:
                                mini = min(mini,a[(i-pow(2,n-j-1),k)]+dis(point[k],point[j]))
                        if mini < float('inf'):
                            a[(i,j)] = mini
    result = float('inf')
    for k in range(1,n):
        result = min(result, a[(pow(2,n)-1,k)] + dis(point[0],point[k]))
    return result

n = 8
tsp(n,point)
