#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:28:13 2019

@author: ayse
"""
"""
Searches for the smallest monthly payment that can pay off the entire balance within a year. 

    Monthly interest rate = (Annual interest rate) / 12.0
    
    Monthly payment lower bound = Balance / 12
    
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Uses bisection search to find the smallest monthly payment to the cent. 
"""

init_balance = balance
monthlyInterestRate = annualInterestRate/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.01

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))
