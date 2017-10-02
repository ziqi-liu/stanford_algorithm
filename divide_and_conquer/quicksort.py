# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:22:36 2017

@author: zliu1
"""
'''
def choosepivot(a,start,end):
    return start
def choosepivot(a,start,end):
    return end    
'''
def choosepivot(a,start,end):
    middle = start + (end - start) // 2
    if a[start] > a[end] and a[end] > a[middle]:
        return end
    if a[middle] > a[end] and a[end] > a[start]:
        return end
    if a[end] > a[start] and a[start] > a[middle]:
        return start
    if a[middle] > a[start] and a[start] > a[end]:
        return start
    return middle
    
    
def quicksort(a,start,end): #count the number of comparision in quicksort
    
    if end <= start:
        return 0
    p = choosepivot(a,start,end)
    a[start],a[p] = a[p],a[start]
    i,j = start + 1, start + 1
    while j <= end:
        if a[j] < a[start]:
            a[i],a[j]=a[j],a[i]
            i += 1
        j += 1
    a[start],a[i-1] = a[i-1], a[start]
    
    return quicksort(a,start,i-2) + quicksort(a,i,end) + end - start

