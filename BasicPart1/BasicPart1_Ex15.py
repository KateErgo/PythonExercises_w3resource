# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:09:24 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 15. Write a Python program to get the volume of a sphere with radius 6.

from math import pi

def vol_sphere(r):
    
    volume = (4/3) * pi * r ** 3
    
    print("The volume of the sphere with radius " + str(r) + " is " + str(volume) + ".")

vol_sphere(6)