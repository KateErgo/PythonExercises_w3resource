# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 10:59:17 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module. 

import calendar

def cal():
    
    year = int(input("Input year: "))
    month = int(input("Input month: "))
    
    return calendar.month(year, month)

cal()