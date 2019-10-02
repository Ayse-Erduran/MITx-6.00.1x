#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:01:18 2019

@author: ayse
"""

def isWordGuessed(secretWord, lettersGuessed):
"""
Takes in two parameters -
    secretWord: a string
    lettersGuessed: a list of letters
Returns a boolean - 
    True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed)
    False otherwise.
"""
    guessed = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessed = False
    return guessed

