# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:00:35 2019

@author: kate
"""

#########################################
### w3resource Python exercises: List ###
#########################################

# 5. Write a Python program to count the number of strings where the string length is 2 or more and 
# the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def Strings(l):
    
    count = 0
    for item in l:
        if len(item) >= 2 and item[0] == item[-1]:
            count += 1
    return count

Strings(['abc', 'xyz', 'aba', '1221'])
    

        