# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def rev(g): #reverse a directed graph
    h = {}
    for e in list(g):
        h[e] = []
    for e in list(g):
        for f in g[e]:
            if f in h:
                h[f].append(e)
            else:
                h[f] = [e]
    return h          
import os
import queue
os.chdir(r"C:\users\zliu1\Desktop")
g = {}
with open("2sat6.txt") as f:
    for line in f:
        l = line.split()
        l = [int(x) for x in l]
        if len(l) ==1:
            for i in range(1,l[0]+1):
                g[i] = []
                g[-i] = []
        else:
            g[-l[0]].append(l[1])
            g[-l[1]].append(l[0])
h = rev(g)
for e in list(h):
    if e not in g:
        g[e] = []
explore = {}
score = []



def scc(g):
   
    result = []
    global explore
    global score
    h = rev(g)
    for e in list(h):
        explore[e] = -1
    # dfs on rev(g)
    for e in list(h):
        if explore[e] == -1:
            explore[e] = 1
            q = queue.LifoQueue()
            q.put(e)
            while not q.empty():
                f = q.get()
                count = 0
                for e in h[f]:
                    if explore[e] == -1:
                        count = 1
                        break
                if count == 0:
                    score.append(f)
                else:
                    q.put(f)
                    for e in h[f]:
                        if explore[e] == -1:
                            explore[e] = 1
                            q.put(e)
             
    # dfs on g

    score = list(reversed(score))
    for e in list(g):
        explore[e] = -1
    for e in score:
        if explore[e] == -1:
            output = []
            explore[e] = 1
            q = queue.LifoQueue()
            q.put(e)
            while not q.empty():
                f = q.get()
                output.append(f)
                for e in g[f]:
                    if explore[e] == -1:
                        explore[e] = 1
                        q.put(e)
            result.append(output)
    return result

def twosat(g):
    s = scc(g)
    for e in s:
        f = [abs(x) for x in e]
        f.sort()
        for i in range(0,len(f)-1):
            if f[i] == f[i+1]:
                return 0
    return 1

twosat(g)
        
#101100