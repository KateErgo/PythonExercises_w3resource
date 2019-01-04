# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:53:57 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5
# Expected Result : 615

n = input("Enter a number: ")

num1 = n
num2 = n * 2
num3 = n * 3
total = int(num1) + int(num2) + int(num3)

print(total)