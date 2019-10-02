#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:39:23 2019

@author: ayse
"""

def getGuessedWord(secretWord, lettersGuessed):
    """
    Takes two parameters:
        secretWord: a string, the word the user is guessing
        lettersGuessed: a list, what letters have been guessed so far
    Returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    result = ""
    for i in secretWord:
        if i in lettersGuessed:
            result += i
        else:
            result += "_"
    return result