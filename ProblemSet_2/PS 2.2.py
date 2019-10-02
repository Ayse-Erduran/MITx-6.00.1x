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


monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)


