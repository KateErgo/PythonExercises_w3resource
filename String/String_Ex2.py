# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:59:44 2019

@author: kate
"""

###########################################
### w3resource Python exercises: String ###
###########################################

# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

from collections import Counter

def countChar():
    
    word = input("Enter a word: ")
    count = Counter(word) 
    print(count)

countChar()