# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:50:24 2024

@author: lotte
"""

#%% Fucntions

def func_diff_lst(lst):
    outp_lst = []
    for i in range(len(lst)-1):
        outp_lst.append(abs(lst[i+1]-lst[i]))
    return outp_lst

def safe_lst(lst):
    safe_val = False
    check_diff = max(func_diff_lst(lst))<4 and min(func_diff_lst(lst))>0
    check_sort = (sorted(lst) == lst) or (sorted(lst, reverse=True) == lst)
    if check_diff and check_sort:
        safe_val = True
    return safe_val

inp = open("./AdventofCode_2.1_input.txt", "r") 

#%% Day 2.1

lines = inp.readlines()
lines_lst = []
for line in lines:
    lines_lst.append([int(n) for n in line.strip().split(' ')])
    
  
# reading the file
#lines = [[int(n) for n in line.strip().split(',')] for line in f.readlines() if line.strip()]
count = 0
for line in lines_lst:
    if safe_lst(line):
        count = count + 1
        
# printing the data
print(count)
#%% Day 2.2
inp = open("./AdventofCode_2.1_input.txt", "r") 
lines = inp.readlines()
lines_lst = []
for line in lines:
    lines_lst.append([int(n) for n in line.strip().split(' ')])

count_2 = 0
for line in lines_lst:
    safe = False
    if safe_lst(line):
        safe = True
    else:
        for i in range(len(line)):
            tmp_lst = line[:i] + line[i+1:]
            if safe_lst(tmp_lst):
                safe = True
    if safe:
        count_2 = count_2+1

print(count_2)