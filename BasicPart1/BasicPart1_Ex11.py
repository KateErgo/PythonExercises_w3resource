# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:08:34 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

def PrintDocs(funcName):
    return help(funcName)

help(abs)