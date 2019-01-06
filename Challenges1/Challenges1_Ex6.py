# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:15:41 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 6. Write a Python program to check if a number is a power of a given base.
# Input : 128,2

def PowOfBase():
    
    base = int(input("Enter base number: "))
    n = int(input("Enter power number: "))

    if base % n == 0:
        return True
    else:
        return False
    
PowOfBase()
    
