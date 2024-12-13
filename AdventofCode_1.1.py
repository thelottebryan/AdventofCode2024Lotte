# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:00:25 2024

@author: lotte
"""
#%% Day 1.1
import numpy as np

inp = np.loadtxt('./AdventofCode_1.1_input.txt')
inp_t = np.transpose(inp)
arr_0 = np.sort(inp_t[0])
arr_1 = np.sort(inp_t[1])
arr_abs = abs(np.subtract(arr_0,arr_1))
answer = sum(arr_abs)
print(answer)

#%% Day 1.2
sim_score = 0

for x in arr_0:
    sim_score = sim_score+x*np.count_nonzero(arr_1 == x)
print(sim_score)