#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:55:56 2019

@author: ayse
"""

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s = "azcbobobegghakl"
numVow = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        numVow += 1
print("Number of vowels: " + str(numVow))
    