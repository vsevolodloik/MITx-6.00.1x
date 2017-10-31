# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:32:09 2016

@author: Vsevold Loik
"""


high = 100
low = 0
ans = 50

print('Please think of a number between 0 and 100!')
while True:
    print('Is your secret number ' + str(ans) + '?')
    n = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if n == 'c':
        break
    elif n == 'h':
        high = ans
    elif n == 'l':
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    ans = int((high + low)/2.0)
print("Game over. Your secret number was: " + str(ans))
    
    
    
# greatest common divisor    
    def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

# is the character in the string?
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    else:
        if aStr[int(len(aStr)/2)] == char:
            return True
        elif aStr[int(len(aStr)/2)] < char:
            return isIn(char, aStr[(int(len(aStr)/2))+1:])
        elif aStr[int(len(aStr)/2)] > char:
            return isIn(char, aStr[:(int(len(aStr)/2))])
    
           
    
    ### polysum
import math
def polysum(n, s):
    """
    takes 2 arguments, n and s
    function should sum the area and square of the perimeter of the regular polygon
    function returns the sum, rounded to 4 decimal places
    """
    area = 0.25*n*s**2/math.tan(math.pi/n)
    perimeter = n*s
    return round(area+perimeter**2, 4)

## Problem Set 2. Exercise 1

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def remaining_balance(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        minimum_monthly_payment = balance*monthlyPaymentRate
        monthly_unpaid_balance = balance - minimum_monthly_payment
        balance = monthly_unpaid_balance*(1+annualInterestRate/12.0)
    return print('Remaining balance:', round(balance, 2))
    
## Problem Set 2. Exercise 2
    
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
 
##   
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
    
## Problem Set 2. Exercise 3

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

##
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

#### a good one (brother)
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

#### good one 2
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