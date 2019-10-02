#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 10:36:25 2019

@author: ayse
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    origTuple = aTup
    newTuple = ()
    
    for i in range(len(origTuple)):
        if i % 2 == 0:
            newTuple += origTuple[i],
    return newTuple
    
print(oddTuples(()))
print(oddTuples((7,)))
print(oddTuples((17, 2, 20, 4, 4, 13)))
print(oddTuples((1, 12, 15, 16, 3, 0, 7, 18, 1, 20)))