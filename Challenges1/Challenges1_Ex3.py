# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:26:49 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 3. Write a Python program to check if a given positive integer is a power of four.

def PowerOfFour():
    number = int(input("Enter any positive number: "))
    if number % 4 == 0:
        return True
    else:
        return False
        
PowerOfFour()