# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:33:10 2024

@author: lotte
"""
import numpy as np

map_lst = open("./AdventofCode_6_input.txt", "r").readlines()
map_lst = [list(line) for line in map_lst]
obstuctions = np.zeros((len(map_lst),len(map_lst[0])))
for i in range(len(map_lst)):
    for j in range(len(map_lst[i])):
        if map_lst[i][j] == "^":
            cl = np.array([i,j])
        elif map_lst[i][j] == "#":
            obstuctions[i][j] = 2

visited_1 = np.zeros((len(map_lst),len(map_lst[0])))
visited_1[cl[0],[cl[1]]] = 1
direction = 1

iter = 0
out_of_bounds = False

while iter<10000 and not(out_of_bounds):
    
    if direction % 4 == 1:
        add = np.array([-1,0])
    elif direction % 4 ==2:
        add = np.array([0,1])
    elif direction % 4 ==3:
        add = np.array([1,0])
    else:
        add = np.array([0,-1])
    nl = cl + add
    if 0<=nl[0]<len(map_lst) and 0<=nl[1]<len(map_lst[0]): #In bounds
        if map_lst[nl[0]][nl[1]] =="#":
            direction = direction + 1
        else:
            cl = nl
            visited_1[cl[0]][cl[1]]=1
    else: # out of bounds
        out_of_bounds = True
    iter = iter + 1

total_route = obstuctions + visited_1
    

#%%
import numpy as np

cycle_count = 0
map_lst = open("./AdventofCode_6_input.txt", "r").readlines()
map_lst = [list(line) for line in map_lst]

for loc_0 in range(len(map_lst)):
    for loc_1 in range(len(map_lst[0])):
        map_lst_tmp = [list(line) for line in open("./AdventofCode_6_input.txt", "r").readlines()]
        if map_lst[loc_0][loc_1]!="#" and map_lst[loc_0][loc_1]!="^" and visited_1[loc_0][loc_1] == 1:
            map_lst_tmp[loc_0][loc_1] = "#"
            visited_arr = np.zeros((len(map_lst),len(map_lst[0])))
            obstuctions = np.zeros((len(map_lst),len(map_lst[0])))
            print("Obstruction placed in location "+str(loc_0)+","+str(loc_1))
            for i in range(len(map_lst)):
                for j in range(len(map_lst[i])):
                    if map_lst_tmp[i][j] == "^":
                        cl = np.array([i,j])
                    elif map_lst_tmp[i][j] == "#":
                        obstuctions[i][j] = 2
            obstuctions[loc_0][loc_1] = 3
            direction = 1
            visited = []
            is_cycle = False
            iter_cnt = 0
            out_of_bounds = False
            
            while iter_cnt<10000 and not(out_of_bounds) and not(is_cycle):
                visited_arr[cl[0]][cl[1]] = 1
                if direction % 4 == 1:
                    add = np.array([-1,0])
                elif direction % 4 ==2:
                    add = np.array([0,1])
                elif direction % 4 ==3:
                    add = np.array([1,0])
                else:
                    add = np.array([0,-1])

                nl = cl + add
                if 0<=nl[0]<len(map_lst) and 0<=nl[1]<len(map_lst[0]): #In bounds
                    if map_lst_tmp[nl[0]][nl[1]] =="#":
                        direction = direction + 1
                    else:
                        cl = nl
                else: # out of bounds
                    out_of_bounds = True

                if ([cl[0],cl[1],direction % 4] in visited) and not out_of_bounds:
                    is_cycle = True
                else:
                    visited.append([cl[0],cl[1],direction % 4])
                iter_cnt = iter_cnt + 1
            total_route_2 = obstuctions + visited_arr
            if is_cycle:
                cycle_count = cycle_count + 1
                print("Cycle found after "+str(iter_cnt)+" moves!")
            del cl, direction, is_cycle
        del map_lst_tmp
            
                    


