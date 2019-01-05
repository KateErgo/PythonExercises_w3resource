# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:26:50 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal 
# then return thrice of their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 + num2 + num3)/3 == num1:
    print((num1 + num2 + num3) * 3)
else:
    print(num1 + num2 + num3)