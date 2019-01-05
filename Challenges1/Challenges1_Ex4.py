# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:27:36 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 4. Write a Python program to check if a number is a perfect square. 

def PerfectSquare():
    number = int(input("Enter a number: "))
    if number % (number ** 0.5) == 0:
        return True
    else:
        return False
    
PerfectSquare()