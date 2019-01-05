# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:26:07 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 2. Write a Python program to check if a given positive integer is a power of three.

def PowerOfThree():
    number = int(input("Enter any positive number: "))
    if number % 3 == 0:
        return True
    else:
        return False
        
PowerOfThree()