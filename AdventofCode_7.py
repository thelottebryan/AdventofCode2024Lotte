# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 12:40:42 2024

@author: lotte
"""
import numpy as np
inp = open("./AdventofCode_7_input.txt", "r").readlines()
inp = [lst.split(':') for lst in inp]
arr_solutions = np.zeros(len(inp))
lst_inp = []
for i in range(len(inp)):
    arr_solutions[i] = inp[i][0]
    lst_inp.append([int(j) for j in inp[i][1].strip().split(" ")])


def recur_function(sol, inp_lst, ind, sol_init, sol_bool):
    #print("Current solution = "+str(sol_init))
    if ind == len(inp_lst)-1:
        if sol == sol_init:
            sol_bool.append(1)
            return sol_bool
        else:
            return sol_bool
            #print("Incorrect solution")
    if sol_init > sol:
        #print("Too large.")
        return sol_bool
    else:
        #print("Go deeper")
        ind = ind + 1
        sol_bool = recur_function(sol, inp_lst, ind, sol_init+inp_lst[ind],sol_bool)
        sol_bool = recur_function(sol, inp_lst, ind, sol_init*inp_lst[ind],sol_bool)
        sol_bool = recur_function(sol, inp_lst, ind, int(str(sol_init)+str(inp_lst[ind])),sol_bool)
        return sol_bool

sol_counter = 0
for cnt in range(len(arr_solutions)):
    res = None
    res = recur_function(arr_solutions[cnt], lst_inp[cnt] , 0, lst_inp[cnt][0],[] )
    if 1 in res:
        sol_counter = sol_counter + arr_solutions[cnt]
