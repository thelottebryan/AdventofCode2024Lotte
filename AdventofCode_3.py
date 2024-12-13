# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:02:03 2024

@author: lotte
"""
import re

inp = open("./AdventofCode_3_input.txt", "r")
string = inp.read()


mult_lst = re.findall("mul\(\d+,\d+\)",string)
mult_tmp=[]
for i in mult_lst:
    i_tmp = i[4:-1].split(",")
    mult_tmp.append(i_tmp)
count_3 = 0

for i in mult_tmp:
    #print(i)
    count_3 = count_3 + int(i[0])*int(i[1])
print(count_3)

#%%3.2
inp = open("./AdventofCode_3_input.txt", "r")
string = inp.read()
#cond_lst = re.findall("do\(\)((?!don't).)*don't\(\)",string)
do_lst = string.split('do()')
cond_lst = []
for string_tmp in do_lst:
    if string_tmp.find("don't()")>0:
        cond_lst.append(string_tmp[:string_tmp.find("don't()")])
    else:
        cond_lst.append(string_tmp)

mult_tmp = []
for cond in cond_lst:
    cond_mult_tmp = re.findall("mul\(\d+,\d+\)",cond)
    for i in cond_mult_tmp:
        i_tmp = i[4:-1].split(",")
        mult_tmp.append(i_tmp)
    del cond_mult_tmp

count_4 = 0
for i in mult_tmp:
    count_4 = count_4 + int(i[0])*int(i[1])
print(count_4)