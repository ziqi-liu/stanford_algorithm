# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:59:48 2017

@author: zliu1
"""
import numpy as np
def p(a,b):
    if a == b:
        return 0
    return 1
v = 0.5
def sequence_alignment(x,y):
    m = len(x)
    n = len(y)
    A = np.zeros((m+1,n+1))
    for i in range(1,m+1):
        A[i][0] = v*i
    for i in range(1,n+1):
        A[0][i] = v*i
    for i in range(1,m+1):
        for j in range(1,n+1):
            A[i][j] = min(A[i-1][j-1]+p(x[i-1],y[j-1]),A[i-1][j]+v, A[i][j-1]+v)
    return A[m][n]
sequence_alignment('aaccccccccccccbbb','aabbvasdjkldladb')
