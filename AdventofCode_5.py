# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:34:56 2024

@author: lotte
"""

lines_rules = open("./AdventofCode_5_inputrules.txt", "r").readlines()
lines_rules = [line.strip().split("|") for line in lines_rules]
lines_manuals = [line.strip().split(",") for line in lines_manuals]
#%%5.1
counter = 0
input_manuals_2 = []
for manual in lines_manuals:
    rules_obeyed = True
    for rule in lines_rules:
        if (rule[0] in manual) and (rule[1] in manual):
            if manual.index(rule[0])>manual.index(rule[1]):
                rules_obeyed = False
    if rules_obeyed:
        counter = counter + int(manual[int(len(manual)/2)])
    else:
        input_manuals_2.append(manual)
#%%5.2
import networkx as nx
counter_2 = 0
for manual in input_manuals_2:
    G = nx.DiGraph()
    G.add_nodes_from(manual)
    for rule in lines_rules:
        if rule[0] in manual and rule[1] in manual:
            G.add_edge(rule[0],rule[1])
    order = nx.tournament.hamiltonian_path(G)
    counter_2 = counter_2 + int(order[int(len(order)/2)])
    del G