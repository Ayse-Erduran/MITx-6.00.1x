#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:53:30 2019

@author: ayse
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    
    If no values in the dictionary, returns None
    '''
    
    # Your Code Here
    myDict = aDict
    biggest = 0
    keyIndex = ''
    for key in myDict.keys():
        if len(myDict[key]) > biggest:
            keyIndex = key
            biggest = len(myDict[key])
    return keyIndex


            
            
        
            
        
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))
