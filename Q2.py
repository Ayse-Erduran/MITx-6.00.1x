#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:05:45 2019

@author: ayse
"""

#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'azcbobobegghakl'
i = 0
times = 0
while i <= len(s)-3:
    if s[i] == "b":
        i += 1
        if s[i] == "o":
            i += 1
            if s[i] == "b":
                times += 1
    else:
        i += 1
print("Number of times bob occurs is: " + str(times))

                