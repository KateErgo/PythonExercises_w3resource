# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:03:27 2019

@author: kate
"""

###########################################
### w3resource Python exercises: String ###
###########################################

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string. 

def newString():
    
    string = input("Enter a string: ")
    if len(string) >= 2:
        new_string = string[0:2] + string[-2:]
        return new_string
    else:
        new_string = ''
        return new_string

newString()
        