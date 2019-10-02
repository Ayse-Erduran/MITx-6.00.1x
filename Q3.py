#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:24:56 2019

@author: ayse
"""

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which 
#the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. 
#For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

s = "tajoltaszoqm"

# initialize variables
i = 0
j = 1
temp = ""
tempLong = ""
#initialize strAlph so that if string s is not in alphabetical order,
#the first character of s prints out
strAlph = s[i]
while i <= len(s) - 2 and j <= len(s) - 1:
    if s[i] > s[j]:
        if len(tempLong) > len(strAlph):
            strAlph = tempLong
        temp = ""
        i += 1
        j += 1
    else:
        temp += s[i]
        tempLong = temp + s[j]
        i += 1
        j += 1


if len(strAlph) >= len(tempLong):
    print(strAlph)
else: 
    print(tempLong)

