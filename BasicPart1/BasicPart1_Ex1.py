# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:19:19 2019

@author: kate
"""

###################################################
### w3resource Python exercises: Basic - Part 1 ###
###################################################

# 1. Write a Python program to print the following string in a specific format (see the output). 
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, 
# Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
#
# Twinkle, twinkle, little star,
#	How I wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#	How I wonder what you are

def Twinkle():
    
    print("\nTwinkle, twinkle, little star," + 
          "\n\tHow I wonder what you are!" +
          "\n\t\tUp above the world so high," +   
          "\n\t\tLike a diamond in the sky." +
          "\nTwinkle, twinkle, little star," + 
          "\n\tHow I wonder what you are")

Twinkle()