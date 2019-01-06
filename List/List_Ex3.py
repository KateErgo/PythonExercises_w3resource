# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:58:11 2019

@author: kate
"""

#########################################
### w3resource Python exercises: List ###
#########################################

# 3. Write a Python program to get the largest number from a list.

def largest(l):
    
    largest_num = sorted(l)[-1]
    
    return largest_num

largest([5,6,12,7,3,9])