# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:38:26 2017

@author: zliu1
"""
def combine(l1,l2): #combine 2 sorted lists
    i,j,result,len1,len2 = 0,0,[],len(l1),len(l2)
    while(1):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
        if i == len1:
            result = result + l2[j:]
            return result
        if j == len2:
            result = result + l1[i:]
            return result

def mergesort(l):#mergesort a list
    lenl = len(l)
    if lenl <= 1:
        return l
    if lenl == 2:
        if l[0] <= l[1]:
            return l
        return [l[1],l[0]]
    cut = lenl // 2
    left = mergesort(l[0:cut])
    right = mergesort(l[cut:lenl])
    return combine(left,right)