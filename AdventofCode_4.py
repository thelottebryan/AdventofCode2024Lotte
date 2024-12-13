# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:28:10 2024

@author: lotte
"""

inp = open("./AdventofCode_4_input.txt", "r") 
lines = inp.readlines()
lines = [line.strip() for line in lines]

print(len(lines[0]))

#%%

def find_words_lst(pos,text):
    lst_words = []
    begin_letter = text[pos[0]][pos[1]]
    dim0 = len(text)
    dim1 = len(text[0])
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            word = begin_letter
            for k in [1,2,3]:
                print(pos[0]+i*k, pos[1]+j*k)
                if pos[0]+i*k>=0 and pos[1]+j*k>=0 and pos[0]+i*k<dim0 and pos[1]+j*k<dim1:
                    word = word + text[pos[0]+i*k][pos[1]+j*k]
            lst_words.append(word)
    return lst_words

def find_words_lst_2(pos,text):
    lst_words = []
    word_x1 = text[pos[0]-1][pos[1]-1]+text[pos[0]][pos[1]]+text[pos[0]+1][pos[1]+1]
    word_x2 = text[pos[0]+1][pos[1]-1]+text[pos[0]][pos[1]]+text[pos[0]-1][pos[1]+1]
    lst_words.append(word_x1[::-1])
    lst_words.append(word_x1)
    lst_words.append(word_x2[::-1])
    lst_words.append(word_x2)
    return lst_words

tmp = find_words_lst_2((1,1),lines)
print(tmp)
print(tmp.count("MAS"))
#%%
counter = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        start_letter = lines[i][j]
        if start_letter == "X":
            tmp_lst_words = find_words_lst((i,j),lines)
            counter = counter + tmp_lst_words.count("XMAS")
#%%
counter_2 = 0
for i in range(1,len(lines)-1):
    for j in range(1,len(lines[0])-1):
        start_letter = lines[i][j]
        if start_letter == "A":
            tmp_lst_words = find_words_lst_2((i,j),lines)
            if tmp_lst_words.count("MAS")==2:
                counter_2 = counter_2 + 1
print(counter_2)