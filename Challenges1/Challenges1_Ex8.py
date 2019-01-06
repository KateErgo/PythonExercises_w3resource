# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:30:38 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 8. Write a Python program to find missing numbers from a list. 

def MissingNumbers(num_list):
    
    orig_list = range(num_list[0], num_list[-1]+1)
    missing = set(orig_list) - set(num_list)
    missing = list(sorted(missing))
    
    return missing

MissingNumbers([1,2,3,4,6,7,10])