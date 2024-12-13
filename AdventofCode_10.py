# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:51:38 2024

@author: lotte
"""

def follow_trail(inp,loc,trails_found):
    if inp[loc[0],loc[1]] == 9:
        #if not loc in trails_found:
        trails_found.append(loc)
        return trails_found
    else:
        directions = []
        if not loc[1]+1 == len(inp[0]):
            if inp[loc[0],loc[1]+1] == inp[loc[0],loc[1]]+1:
                directions.append([0,1])
        if not loc[1]-1 == -1:
            if inp[loc[0],loc[1]-1] == inp[loc[0],loc[1]]+1:
                directions.append([0,-1])
        if not loc[0]+1 == len(inp):
            if inp[loc[0]+1,loc[1]] == inp[loc[0],loc[1]]+1:
                directions.append([1,0])
        if not loc[0]-1 == -1:
            if inp[loc[0]-1,loc[1]] == inp[loc[0],loc[1]]+1:
                directions.append([-1,0])
        if len(directions)==0:
            return trails_found
        else:
            for d in directions:
                trails_found = follow_trail(inp,[loc[0]+d[0],loc[1]+d[1]],trails_found)
            return trails_found
        return trails_found




#%%
import numpy as np
inp = open("./AdventofCode_10_input.txt", "r").read().splitlines()
inp = [[int(j) for j in list(i)] for i in inp]

inp= np.array([inp])[0,:,:]
sol = 0

for i in range(len(inp)):
    for j in range(len(inp[0])):
        if int(inp[i,j]) == 0:
            print("Trailhead found at location ",i,j)
            solution = follow_trail(inp,[i,j],[])
            sol += len(solution)
            print(len(solution))
            print(sol)
            #try recursion
#%%
solution = follow_trail(inp,[0,4],[])
print(len(solution))