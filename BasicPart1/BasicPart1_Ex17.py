# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:23:09 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

num = int(input("Enter a number: "))

if num in range(1000 - 100, 1000 + 100):
    print(True)
    print("Number is in range of 1000.")
elif num in range(2000 - 100, 2000 + 100):
    print(True)
    print("Number is in range of 2000.")
else:
    print(False)
    print("Number not in range.")