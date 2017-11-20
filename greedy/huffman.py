# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:23:52 2017

@author: zliu1
"""
import binarytree as bt

def huffman(inp): #input as a list [[p1,'s1'],[p2,'s2']...]
    inp.sort(reverse = True)
    if len(inp) == 2:
        result = []
        result.append('')
        result.append(inp[0][1])
        result.append(inp[1][1])
        return result
    b = inp.pop()
    a = inp.pop()
    inp.append([a[0]+b[0],a[1]+b[1]])
    result = huffman(inp)
    i = result.index(a[1]+b[1])
    result[i] = ''
    while len(result) < 2*i + 3:
        result.append('')
    result[2*i+1] = a[1]
    result[2*i+2] = b[1] 
    return result
#output: a list representing binary tree