# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:59:57 2019

@author: kate
"""

#########################################
### w3resource Python exercises: List ###
#########################################

# 4. Write a Python program to get the smallest number from a list.

def largest(l):
    
    largest_num = sorted(l)[0]
    
    return largest_num

largest([5,6,12,7,3,9])