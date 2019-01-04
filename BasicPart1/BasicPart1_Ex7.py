# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:46:44 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 7. Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java

filename = input("Enter filename: ")

extension = filename.split('.')[1]
print(extension)
