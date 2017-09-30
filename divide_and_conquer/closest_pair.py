# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 19:56:24 2017

@author: zliu1
"""
# closestpair_presort()
# input: a list of points in R^2, p=[[x1,y1],[x2,y2]...]
# output: a pair of points that are closest to each other
def combine(l1,l2,n): #combine 2 sorted lists
    i,j,result,len1,len2 = 0,0,[],len(l1),len(l2)
    while(1):
        if l1[i][n] <= l2[j][n]:
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

def mergesortby(l,n):#mergesort l by index n
    lenl = len(l)
    if lenl <= 1:
        return l
    if lenl == 2:
        if l[0][n] <= l[1][n]:
            return l
        return [l[1],l[0]]
    cut = lenl // 2
    left = mergesortby(l[0:cut],n)
    right = mergesortby(l[cut:lenl],n)
    return combine(left,right,n)

def dist(a,b):
    result,i,n = 0,0,len(a)
    while i < n:
        result += (a[i] - b[i]) ** 2
        i += 1
    return result ** 0.5

def closestpair_presort(p):
    #0. sort by x and y
    px=mergesortby(p,0)
    py=mergesortby(p,1) 
    return closestpair(px,py)
def closestpair(px,py): #p = [[x1,y1],[x2,y2],[x3,y3]...]
    n = len(px)
    if n == 2:
        return [px[0],px[1]]
    if n == 3:
        len01 = dist(px[0],px[1])
        len12 = dist(px[1],px[2])
        len02 = dist(px[0],px[2])
        if len01 <= len12 and len01 <= len02:
            return [px[0],px[1]]
        elif len12 <= len02:
            return [px[1],px[2]]
        return [px[0],px[2]]
    #1. divide by half and return qx,qy,(left),Rx,Ry(right)
    cut = n//2 - 1 #the last point on the left
    xcut = px[cut][0]
    qx = px[:cut + 1]
    rx = px[cut + 1:]
    i,qy,ry = 0,[],[]
    while i < n:
        if py[i][0] > xcut:
            ry.append(py[i])
        else:
            qy.append(py[i])
        i += 1

    #2. recursive
    pair1 = closestpair(qx,qy)
    pair2 = closestpair(rx,ry)
    pair = pair2
    d = min(dist(pair1[0],pair1[1]),dist(pair2[0],pair2[1]))
    if d == dist(pair1[0],pair1[1]):
        pair = pair1
    #3. calculate closest distance in between
    i = 0
    while i < n:
        j = 1
        while j < min(7,n-i):
            if dist(py[i],py[i+j]) < d:
                pair = [py[i],py[i+j]]
                d = dist(py[i],py[i+j])
            j += 1
        i += 1
    return pair

            
