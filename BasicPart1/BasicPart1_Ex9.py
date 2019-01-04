# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:51:07 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
day, month, year = exam_st_date

print("The examination will start from : " + str(day) + " / " + str(month) + " / " + str(year))