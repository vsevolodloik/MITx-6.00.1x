# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:54:37 2017

@author: Vsevolod Loik
"""

## Problem Set 2. 
# Exercise 1

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def remaining_balance(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        minimum_monthly_payment = balance*monthlyPaymentRate
        monthly_unpaid_balance = balance - minimum_monthly_payment
        balance = monthly_unpaid_balance*(1+annualInterestRate/12.0)
    return print('Remaining balance:', round(balance, 2))
    
#Exercise 2
    
def lowest_payment(balance, annualInterestRate):
    guess = 10
    while True:
        new_balance = balance
        for i in range(12):
            monthly_unpaid_balance = new_balance - guess
            new_balance = monthly_unpaid_balance*(1+annualInterestRate/12.0)
        if new_balance > 0:
            guess += 10
        else:
            break
    return print('Lowest payment:', guess)
 
# Exersice 2 - alternative solution  
air = annualInterestRate
mir = air/12

t = 0
b = balance
p = 0

while b > .0001:
    t = 0
    b = balance
    p += 10
    while t < 12:
        b = (b-p) + mir*(b-p)
        t += 1
print 'Lowest Payment: ' + str(p)
    
# Exercise 3

def lowest_payment_bisection(balance, annualInterestRate):
    '''
    function finds the lowest payment to pay out the debt within one year using the bisection search
    '''
    monthlyInterestRate = annualInterestRate/12
    lower = balance/12.0
    upper = (balance*(1+monthlyInterestRate )**12)/12.0
    
    while True:
        new_balance = balance
        guess = (lower + upper)/2
        for i in range(12):
            new_balance = (new_balance - guess)*(1+monthlyInterestRate)
        if new_balance > 0.01:      #guess is too low   
            lower = guess
        elif new_balance < -0.01:    #guess is too high
            upper = guess
        else:                    #balance equals zero +/- 1 cent
            break
    return print('Lowest payment:', round(guess, 2))

# Exercise 3 - alternative solution
def lowest_payment_bisection(balance, annualInterestRate):
    
    monthlyInterestRate = annualInterestRate/12
    lower = balance/12
    upper = (balance*(1+monthlyInterestRate )**12)/12.0
    guess = round((lower + upper)/2, 4)
    while True:
        new_balance = balance
        for i in range(12):
            monthly_unpaid_balance = new_balance - guess
            new_balance = monthly_unpaid_balance*(1+monthlyInterestRate)
        if new_balance > 0.01:      #guess is too low   
            lower = guess
            guess = round((guess + upper)/2, 4)
        elif new_balance < -0.01:    #guess is too high
            upper = guess
            guess = round((lower + guess)/2, 4)
        else:                    #balance equals zero +/- 1 cent
            break
    return print('Lowest payment:', guess)

# Exercise 3 - alternative solution 2 (brother)
balance = 999999
annualInterestRate = 0.18

air = annualInterestRate
mir = air/12

b = float(balance)
l = 0
h = b
p = (l+h)/2

while True:
    b = float(balance)
    p = (l+h)/2
    for t in range(12):
        b = (b-p) + mir*(b-p)
    if b < 0:
        h = p
    elif b > .0001:
        l = p
    else:
        break
print ('Lowest Payment: ' + "%.2f"%(p))

#Exercise 3 - alternative solution 3
balance = 999999
annualInterestRate = 0.18

air = annualInterestRate
mir = air/12

b = float(balance)
l = 0
h = b
p = (l+h)/2

while b > .0001 or b < 0:
    b = float(balance)
    p = (l+h)/2
    for t in range(12):
        b = (b-p) + mir*(b-p)
    if b < 0:
        h = p
    elif b > .0001:
        l = p
        
print ('Lowest Payment: ' + "%.2f"%(p))