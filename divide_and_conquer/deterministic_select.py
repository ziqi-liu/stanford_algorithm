# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def select(a,k): #select the kth statistic in list a in O(n), do not use randomization
    l = len(a)
    if l <= 5 :
        a.sort()
        return a[k-1]
    c = []
    i = 0
    while i < l:
        if i + 4 < l:
            c.append(select(a[i:i+5],3))
            i += 5
        else:
            c.append(select(a[i:],(l - i + 1) // 2))
            break
    print(c)
    p = select(c,(len(c)+1)//2)
    a[0],p = p,a[0]
    i,j = 1,1
    while j < l:
        if a[j] < a[0]:
            a[i],a[j]=a[j],a[i]
            i += 1
        elif a[j] == a[0]:
            a[j] = p
            if a[j] < a[0]:
                a[i],a[j]=a[j],a[i]
                i += 1
        j += 1
    if i == k:
        return a[0]
    if i < k:
        return select(a[i:],k-i)
    return select(a[1:i],k)
    



