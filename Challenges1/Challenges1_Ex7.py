# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:21:22 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Challenges - 1 ###
###################################################

# 7. Write a Python program to find a missing number from a list.
# Input : [1,2,3,4,6,7,8]
# Output : 5

def MissingNum(num_list): 
   
    return sum(range(num_list[0],num_list[-1]+1)) - sum(num_list)

print(MissingNum([1,2,3,4,6,7,8]))