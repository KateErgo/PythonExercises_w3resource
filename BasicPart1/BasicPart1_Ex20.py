# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:54:03 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def nStrings():
    
    string = input("Enter a string: ")
    n = int(input("How many copies do you want? "))
    
    return n * string

nStrings()