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
with open("SCC.txt") as f:
    for line in f:
        l = line.split()
        if l[0] not in g:
            g[l[0]] = [l[1]]
        else:
            g[l[0]].append(l[1])
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

p = scc(g)
q = [len(x) for x in p]
q.sort(reverse=True)
print(q[:5])


