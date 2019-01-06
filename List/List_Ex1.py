# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:46:20 2019

@author: kate
"""

#########################################
### w3resource Python exercises: List ###
#########################################

# 1. Write a Python program to sum all the items in a list. 

def sumList(l):
    
    tot = 0
    for num in l:
        tot += num
    return tot
    
sumList([1, 2, 3])