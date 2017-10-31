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
    
           
    
## polysum
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

