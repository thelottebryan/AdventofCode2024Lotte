# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:31:36 2024

@author: lotte
"""

print(2*"p")
#%%
import numpy as np
inp_str = open("./AdventofCode_9_input.txt", "r").read()
#inp_str = "2333133121414131402"
inp_lst= list(inp_str)

#%%
counter = 0
file_id = 0
tmp_lst = []
for i in range(len(inp_lst)):
    if i%2 == 0:
        add = [file_id]*int(inp_lst[counter])
        tmp_lst = tmp_lst + add
        file_id = file_id + 1
    else:
        add = ["."]*int(inp_str[counter])
        tmp_lst = tmp_lst + add
    counter = counter + 1
#%%
empty_ind_lst = [ind for ind, ele in enumerate(tmp_lst) if ele == "."]

ind=0
i=0
while empty_ind_lst[ind] < (len(tmp_lst)-i):
    if tmp_lst[-i-1] != ".":
        tmp_lst[empty_ind_lst[ind]]=tmp_lst[-i-1]
        tmp_lst[-i-1] = "."
        ind +=1
    i+=1

#%%
end_reached = False
sum_tot = 0
i = 0
while not(end_reached):
    sum_tot = sum_tot+tmp_lst[i]*i
    i+=1
    if tmp_lst[i] == ".":
        end_reached = True

#%%9.2
import numpy as np
inp_str = open("./AdventofCode_9_input.txt", "r").read()
#inp_str = "2333133121414131402"
inp_lst= list(inp_str)

counter = 0
file_id = 0
tmp_lst = []
empty_spaces = np.empty((0,2),int)
filled_spaces = np.empty((0,3),int)
len_str = 0
for i in range(len(inp_lst)):
    if i%2 == 0:
        add = [file_id]*int(inp_lst[counter])
        filled_spaces = np.append(filled_spaces, np.array([[len_str,file_id,int(inp_lst[counter])]]), axis = 0)
        tmp_lst = tmp_lst + add
        file_id = file_id + 1
        len_str = len_str+int(inp_lst[counter])
    else:
        add = ["."]*int(inp_str[counter])
        tmp_lst = tmp_lst + add
        empty_spaces = np.append(empty_spaces, np.array([[len_str,int(inp_lst[counter])]]), axis=0)
        len_str = len_str+int(inp_lst[counter])
    counter = counter + 1
#%%
print(max(empty_spaces[:,1]))
#%%
for i in range(len(filled_spaces)):
    el = filled_spaces[len(filled_spaces)-1-i,:]
    if max(empty_spaces[:,1])>=el[2]:
        space_found = False
        ind_too_high = False
        j=0
        while not space_found and not ind_too_high:
            if empty_spaces[j,1]>=el[2]:
                if el[0]<empty_spaces[j,0]:
                    ind_too_high = True
                else:
                    move_to = empty_spaces[j,:]
                    space_found = True
                    for k in range(el[2]):
                        tmp_lst[move_to[0]+k] = el[1]
                        tmp_lst[el[0]+k] = "."
                    empty_spaces[j,1]-=el[2]
                    empty_spaces[j,0]+=el[2] 
            j+=1
#%%
sum_tot = 0
for i in range(len(tmp_lst)):
    if tmp_lst[i]!=".":
        sum_tot = sum_tot+int(tmp_lst[i])*i

