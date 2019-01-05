# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:20:41 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 16. Write a Python program to get the difference between a given number and 17, if the number is greater 
# than 17 return double the absolute difference.

num = int(input("Enter a number of your choice: "))

if num <= 17:
    diff = 17 - num
    print(diff)
else:
    diff = abs(17 - num) * 2
    print(diff)