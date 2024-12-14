# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:39:13 2024

@author: lotte
"""
import numpy as np
import re
import math as m
inp_lst = open("./AdventofCode_14_input.txt", "r").readlines()
inp_par = [[int(num) for num in re.findall(r'[-]?\d+',line)] for line in inp_lst]
#%%14.1
dim0=103
dim1=101
sec = 100
robots_endloc = np.zeros((dim0,dim1))
for r in inp_par:
    p = np.array([r[0],r[1]])
    v = np.array([r[2],r[3]])
    loc = [(p[0]+sec*v[0])%dim1,(p[1]+sec*v[1])%dim0]
    robots_endloc[loc[1],loc[0]] +=1
q1 = robots_endloc[0:m.floor(dim0/2),0:m.floor(dim1/2)]
q2 = robots_endloc[0:m.floor(dim0/2),m.ceil(dim1/2):dim1]
q3 = robots_endloc[m.ceil(dim0/2):dim0,0:m.floor(dim1/2)]
q4 = robots_endloc[m.ceil(dim0/2):dim0,m.ceil(dim1/2):dim1]
sf = np.sum(q1)*np.sum(q2)*np.sum(q3)*np.sum(q4)

#%%14.2
dim0=103
dim1=101
secs_max = 10000
sym_index = float('inf')
sym_sec = 0
for sec in range(secs_max):
    robots_endloc = np.zeros((dim0,dim1))
    locs0 = []
    locs1 = []
    for r in inp_par:
        p = np.array([r[0],r[1]])
        v = np.array([r[2],r[3]])
        loc = [(p[0]+sec*v[0])%dim1,(p[1]+sec*v[1])%dim0]
        locs0.append(loc[0])
        locs1.append(loc[1])
        robots_endloc[loc[1],loc[0]] =1
    var0 = np.var(np.array(locs0))
    var1 = np.var(np.array(locs1))
    #print("For second "+str(sec)+", christmas tree index equals: "+str(var0*var1))
    if var0*var1<sym_index:
        sym_sec = sec
        sym_index = var0*var1
        
#%%

sec = 7916
robots_endloc = np.zeros((dim0,dim1))
for r in inp_par:
    p = np.array([r[0],r[1]])
    v = np.array([r[2],r[3]])
    loc = [(p[0]+sec*v[0])%dim1,(p[1]+sec*v[1])%dim0]
    robots_endloc[loc[1],loc[0]] +=1