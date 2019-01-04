# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:40:46 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list 
# and a tuple with those numbers. 
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

numbers = input("Please enter a list of comma-separated numbers: ")

print(numbers.split(','))
print(tuple(numbers.split(',')))