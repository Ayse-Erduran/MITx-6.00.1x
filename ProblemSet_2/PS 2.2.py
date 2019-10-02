#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:18:14 2019

@author: ayse
"""

"""
Calculates the minimum fixed monthly payment to pay off a credit card balance
within 12 months. 

balance: the outstanding balance on the credit card

annualInterestRate: annual interest rate as a decimal

Returns the lowest monthly payment that will pay off all debt in under 1 year. 
"""

balance = 3329
annualInterestRate = 0.2
initBalance = balance 

minFixed = 0

while True:
    for i in range(12):
        balance = (balance - minFixed) + (balance - minFixed) * annualInterestRate / 12
    if balance > 0:
        minFixed += 10
        balance = initBalance
    else:
        False
        
print("Lowest payment: " + str(minFixed))
