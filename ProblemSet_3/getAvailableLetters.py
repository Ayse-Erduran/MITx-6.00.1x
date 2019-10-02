#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:20:57 2019

@author: ayse
"""

def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    Returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    """
    result = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in alph:
        if i not in lettersGuessed:
            result += i
    return result


            

    