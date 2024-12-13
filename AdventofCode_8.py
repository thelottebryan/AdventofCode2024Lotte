# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:21:42 2024

@author: lotte
"""
import numpy as np
inp = open("./AdventofCode_8_input.txt", "r").read().splitlines()
inp = [list(i) for i in inp]

bool_arr = np.zeros((len(inp),len(inp[0])))

for j in range(len(inp[0])):
    for i in range(len(inp)):
        print("Looking for nodes in line "+str(i))
        if inp[i][j] != '.' and inp[i][j] != '#':
            char = inp[i][j]
            for k in range(len(inp)):
                for l in range(j,len(inp[0])):
                    if not((k==i)and(l==j)) and inp[k][l] == char:
                        for res in range(int(len(inp)/max(k-i,l-j))+1):
                            no_1_0 = k+res*(k-i)
                            no_1_1 = l+res*(l-j)
                            no_2_0 = i-res*(k-i)
                            no_2_1 = j-res*(l-j)
                            if (0<=no_1_0<len(inp))and(0<=no_1_1<len(inp[0])):
                                bool_arr[no_1_0][no_1_1] = 1
                            if (0<=no_2_0<len(inp))and(0<=no_2_1<len(inp[0])):
                                bool_arr[no_2_0][no_2_1] = 1
print(sum(sum(bool_arr)))