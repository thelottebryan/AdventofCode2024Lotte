# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 07:51:40 2024

@author: lotte
"""



#%%
#Recursieve formule om voor alle plots te vinden
def find_patch(inp,init,patch):
    patch[init[0],init[1]] = 1
    if init[0]-1>=0: #search west
        if patch[init[0]-1,init[1]] != 1 and inp[init[0]-1][init[1]] == inp[init[0]][init[1]]:
            patch = find_patch(inp,(init[0]-1,init[1]),patch)
    if init[0]+1<len(inp): #search east
        if patch[init[0]+1,init[1]] != 1 and inp[init[0]+1][init[1]] == inp[init[0]][init[1]]:
            patch = find_patch(inp,(init[0]+1,init[1]),patch)
    if init[1]-1>=0:
        if patch[init[0],init[1]-1] != 1 and inp[init[0]][init[1]-1] == inp[init[0]][init[1]]:
            patch = find_patch(inp,(init[0],init[1]-1),patch)
    if init[1]+1<len(inp[0]):
        if patch[init[0],init[1]+1] != 1 and inp[init[0]][init[1]+1] == inp[init[0]][init[1]]:
            patch = find_patch(inp,(init[0],init[1]+1),patch)
    return patch

def find_borders(arr):
    bords = []
    if len(arr)==0:
        return []
    else:
        arr = np.sort(arr)
        #print(arr)
        bord = str(max(arr))+"-"+str(max(arr)+1)
        bords.append(bord)
        bord = str(min(arr))+"-"+str(min(arr)-1)
        bords.append(bord)
        for i in range(len(arr)-1):
            if arr[i+1]!=arr[i]+1:
                bord = str(arr[i])+"-"+str(arr[i]+1)
                bords.append(bord)
                bord = str(arr[i+1])+"-"+str(arr[i+1]-1)
                bords.append(bord)
        return bords
        
def find_no_horz_borders(patch):
    inds = np.where(patch == 1)
    no_horz_borders = len(find_borders(inds[0][np.where(inds[1]==min(inds[1]))]))
    for col in set(inds[1]):
        row_inds = inds[0][np.where(inds[1]==col)]
        row_inds_next = inds[0][np.where(inds[1]==col+1)]
        bord_1 = find_borders(row_inds)
        bord_2 = find_borders(row_inds_next)
        #print("In column "+str(col)+" we have "+str(len(bord_1))+" borders. The borders are located at "+str(bord_1)+". The borders of the next column are located at "+str(bord_2)+".")
        diff_board = []
        for i in bord_2:
            if i in bord_1:
                bord_1.remove(i)
            else:
                diff_board.append(i)
        no_horz_borders += len(diff_board)
        #print("The additional borders in the next row are "+str(diff_board)+".")
    return no_horz_borders

#%%9.2
import numpy as np
import numpy.ma as ma
inp_lst = open("./AdventofCode_12_input.txt", "r").readlines()
inp_lst= [list(i.strip()) for i in inp_lst]

safety = 0
full_sum = 0
searched = np.zeros((len(inp_lst),len(inp_lst[0])))

full_cost = 0
while safety <10000 and full_sum < len(inp_lst)*len(inp_lst[0]):
    nl = np.array([arr[0] for arr in np.where(searched == 0)])
    #Compute area
    res_patch = find_patch(inp_lst,(nl[0],nl[1]),np.zeros((len(inp_lst),len(inp_lst[0]))))
    area = np.sum(res_patch)
    perimiter = find_no_horz_borders(res_patch)*2
    print("Region "+str(inp_lst[nl[0]][nl[1]])+" has an area of "+str(area)+" and a perimiter of "+str(perimiter)+".")
    full_cost += area*perimiter
    searched = searched + res_patch
    full_sum = int(np.sum(searched))
    safety += 1
    
print("Full cost is "+str(full_cost))

#%%9.1
safety = 0
full_sum = 0
searched = np.zeros((len(inp_lst),len(inp_lst[0])))

#Array met kosten van het bouwen van een hek voor een bepaald item
fence_array = np.zeros((len(inp_lst),len(inp_lst[0])))
for i in range(len(fence_array)):
    for j in range(len(fence_array[0])):
        cost = 0
        #Check west
        if i-1>=0:
            if inp_lst[i-1][j] != inp_lst[i][j]:
                cost = cost + 1
        else:
            cost = cost + 1
        #Check east
        if i+1<len(inp_lst):
            if inp_lst[i+1][j] != inp_lst[i][j]:
                cost = cost + 1
        else:
            cost = cost + 1
        #Check north
        if j-1>=0:
            if inp_lst[i][j-1] != inp_lst[i][j]:
                cost = cost + 1
        else:
            cost = cost + 1
        #Check south
        if j+1<len(inp_lst[0]):
            if inp_lst[i][j+1] != inp_lst[i][j]:
                cost = cost + 1
        else:
            cost = cost + 1
        fence_array[i][j]=cost

full_cost = 0
while safety <10000 and full_sum < len(inp_lst)*len(inp_lst[0]):
    nl = np.array([arr[0] for arr in np.where(searched == 0)])
    res_patch = find_patch(inp_lst,(nl[0],nl[1]),np.zeros((len(inp_lst),len(inp_lst[0]))))
    area = np.sum(res_patch)
    cost_patch = ma.masked_array(fence_array, np.logical_not(res_patch))
    perimiter = np.sum(cost_patch)
    full_cost += area*perimiter
    searched = searched + res_patch
    full_sum = int(np.sum(searched))
    safety += 1

#%%



