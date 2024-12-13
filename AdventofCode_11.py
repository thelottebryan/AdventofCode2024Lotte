# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:45:03 2024

@author: lotte
"""



def blink_hash(inp,no_blinks,hashmap):
    global function_calls
    function_calls += 1
    key_hm = str(inp)+","+str(no_blinks)
    if key_hm in hashmap: #First check if key is already in hashmap.
        return hashmap[key_hm]
    else: #If key is not in hasmap, compute it and add it.
        if no_blinks == 1: #if we only need to blink once, we know the outcome.
            if inp==0:
                res = 1
            elif len(str(inp))%2 == 0:
                res = 2
            else:
                res = 1
        else: #if we need to blink more often, we break down the problem.
            if inp==0:
                res = blink_hash(1,no_blinks-1,hashmap)
            elif len(str(inp))%2 == 0:
                brk = int(len(str(inp))/2)
                el1 = int(str(inp)[:brk])
                el2 = int(str(inp)[brk:])
                res = blink_hash(el1,no_blinks-1,hashmap) + blink_hash(el2,no_blinks-1,hashmap)
            else:
                res = blink_hash(inp*2024,no_blinks-1,hashmap)
        hashmap[key_hm] = res
        return hashmap[key_hm]



#%%
import timeit
inp_lst = [510613, 358, 84, 40702, 4373582, 2, 0, 1584]
blinks = 75

hashmap = {}
cntr = 0
function_calls = 0
start = timeit.default_timer()
for i in inp_lst:
    cntr += blink_hash(i,blinks,hashmap)
stop = timeit.default_timer()
print("blink_hash took "+ str(stop-start)+ " seconds and " + str(function_calls) + " function calls.")

