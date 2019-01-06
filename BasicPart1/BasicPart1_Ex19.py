# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:43:14 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

def Strings():
    given_string = input("Enter a string: ")
    is_string = "Is "
    new_string = is_string + given_string
    
    if given_string[0:3] == is_string:
        return given_string
    else:
        return new_string
    
Strings()