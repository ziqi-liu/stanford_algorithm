# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:38:26 2017

@author: zliu1
"""
# count the inversion I(k1,k2,...kn) in O(nlogn)
def combine(l1,l2): #combine 2 sorted lists and count inversion
    i,j,l,n,len1,len2 = 0,0,[],0,len(l1),len(l2)
    while(1):
        if l1[i] <= l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            n += len1-i
            j += 1
        if i == len1:
            l = l + l2[j:]
            return n,l
        if j == len2:
            l = l + l1[i:]
            return n,l

def countinversion(l):#mergesort a list and then count inversion
    lenl = len(l)
    if lenl <= 1:
        return 0,l
    if lenl == 2:
        if l[0] <= l[1]:
            return 0,l
        else:
            l[0],l[1] = l[1],l[0]
            return 1,l
    cut = lenl // 2
    left, l1 = countinversion(l[0:cut])
    right,l2 = countinversion(l[cut:lenl])
    between,l = combine(l1,l2)
    return left + right + between, l

