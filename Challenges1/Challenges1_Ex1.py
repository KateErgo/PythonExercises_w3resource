# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:20:34 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 1. Write a Python program to check if a given positive integer is a power of two.

def PowerOfTwo():
    number = int(input("Enter any positive number: "))
    if number % 2 == 0:
        return True
    else:
        return False
        
PowerOfTwo()