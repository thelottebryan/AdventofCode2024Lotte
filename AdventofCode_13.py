# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 07:58:10 2024

@author: lotte
"""
import scipy.optimize as so
import re

#%%13.1
inp_lst = open("./AdventofCode_13_input.txt", "r").readlines()
sums = []
for i in range(int((len(inp_lst)+1)/4)):
    inp_tmp = inp_lst[4*i]+inp_lst[4*i+1]+inp_lst[4*i+2]
    sums.append(inp_tmp)

cntr = 0
for i in sums:
    inp_par = re.findall(r'\d+',i)
    c = [3,1]
    A_eq = [[inp_par[0],inp_par[2]],[inp_par[1],inp_par[3]]]
    b_eq = [inp_par[4],inp_par[5]]
    bounds_1 = (0,100)
    bounds_2 = (0,100)
    res = so.linprog(c,A_eq=A_eq,b_eq=b_eq,bounds=(bounds_1,bounds_2),integrality=(1,1))
    if not res["fun"] == None:
        cntr = cntr + res["fun"]
print(cntr)

#%%13.2
inp_lst = open("./AdventofCode_13_input.txt", "r").readlines()
sums = []
for i in range(int((len(inp_lst)+1)/4)):
    inp_tmp = inp_lst[4*i]+inp_lst[4*i+1]+inp_lst[4*i+2]
    sums.append(inp_tmp)
z = 10000000000000
cntr = 0
for i in sums:
    inp_par = [int(par) for par in re.findall(r'\d+',i)]
    a=inp_par[0]
    b=inp_par[2]
    c=inp_par[1]
    d=inp_par[3]
    e=inp_par[4]
    f=inp_par[5]
    if (a*d-b*c) != 0:
        x1 = ((z+e)*d - (z+f)*b)/(a*d-b*c)
        x2 = ((z+f)*a - (z+e)*c)/(a*d-b*c)
        print(x1.is_integer(), x2.is_integer())
        if x1.is_integer() and x2.is_integer():
            cntr = cntr + x1*3+x2