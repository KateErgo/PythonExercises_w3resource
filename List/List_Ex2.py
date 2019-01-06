# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:55:56 2019

@author: kate
"""

#########################################
### w3resource Python exercises: List ###
#########################################

# 2. Write a Python program to multiplies all the items in a list. 

def multiplyList(l):
    
    tot = 1
    for num in l:
        tot = tot * num
    return tot

multiplyList([1,2,3,4])
    