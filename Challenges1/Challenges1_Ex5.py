# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:38:04 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 5. Write a Python program to check if an integer is the power of another integer.

def PowerOfAnother():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    if number1 % (number2 ** 2) == 0:
        return True
    else:
        return False
    
PowerOfAnother()