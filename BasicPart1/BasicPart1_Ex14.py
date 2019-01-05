# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:13:23 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days 

from datetime import date

firstDate = date(2014, 7, 2)
secondDate = date(2014, 7, 11)

numOfDays = secondDate - firstDate

print(numOfDays)
