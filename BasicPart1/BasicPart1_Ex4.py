# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:29:38 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.

import math
def ComputeArea():
    
    radius = int(input("What is the radius of the circle? "))
    area = radius ** 2 * math.pi 
    print("The area of the circle is: " + str(area) + ".")

ComputeArea()