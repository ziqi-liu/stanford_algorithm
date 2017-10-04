# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
def select(a,k): #select the kth statistic in list a in O(n)
    l = len(a)
    if l == 1:
        return a[0]
    p = random.randint(0,l-1)
    a[0],a[p] = a[p],a[0]
    i,j = 1,1
    while j < l:
        if a[j] < a[0]:
            a[i],a[j]=a[j],a[i]
            i += 1
        j += 1
    if i == k:
        return a[0]
    if i < k:
        return select(a[i:],k-i)
    return select(a[1:i],k)
    



