# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:49:22 2017

@author: Vsevold Loik
"""

# Problem 4
# Write a function is_triangular that meets the specification below. 
# A triangular number is a number obtained by the continued summation of integers starting from 1. 
# For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    counter = 2
    mysum = 1
    if k == 1:
        return True
    else:
        while mysum <= k:
            mysum = mysum + counter
            #print(mysum)
            counter += 1
            if mysum == k:
                return True
    return False
        
# Problem 5
# Write a Python function that takes in a string and prints out a version of this string 
# that does not contain any vowels, according to the specification below. 
# Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sNew = ''
    for i in s:
        if i not in vowels:
            sNew = sNew + i
            #print(sNew)
    print(sNew)
    
    
# Problem 6
# Write a function that satisfies the following docstring:
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    assert not len(L) == 0, 'L is empty'
    assert type(L) == list, 'L is not a list'
    while len(L) > 0:
        largest = max(L)
        counter = 0
        for i in L:
            if i == largest:
                counter += 1
        if counter % 2 == 1:
            return largest
        else:
            for i in range(counter):
                L.remove(largest)
            
            
# Problem 7
# Write a function called dict_invert that takes in a dictionary with immutable 
# values and returns the inverse of the dictionary. The inverse of a dictionary
# d is another dictionary whose keys are the unique dictionary values in d. 
# The value for a key in the inverse dictionary is a sorted list (increasing order) 
# of all keys in d that have the same value in d.
            
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    inverse = {}    
    for i in d.keys():
        if d[i] in inverse:
            #inverse[d[i]].append(i)
            inverse[d[i]] += [i]            
        else:
            inverse[d[i]] = [i]
    for j in inverse.values():
        j.sort()
    return inverse
     
     
     
# Problem 8 
     
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def poly (x):
        result = 0
        for i in range(len(L)):
            result += L[i] * x**(len(L)-1-i)
            #print(result)
        return result
    return poly
    
    
# Problem 9     
    
# Write a Python function that takes in two lists and calculates whether they 
# are permutations of each other. The lists can contain both integers and strings. 

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    # Create an empty dictionary for every list
    dictL1 = {}
    dictL2 = {}
    # populate dictionary with keys, which are list values 
    # and values which are number of occurance in a list
    for elm in L1:
        if elm in dictL1:
            dictL1[elm] += 1
        else:
            dictL1[elm] = 1
    for elm in L2:
        if elm in dictL2:
            dictL2[elm] += 1
        else:
            dictL2[elm] = 1
    if dictL1 == dictL2:
        # find the maximum value
        values = dictL1.values()      
        best = max(values)
        # iterate over dictionary values to find wich one equals maximum value
        # and return its key, the number of occurances, and type        
        for i in dictL1:
            if dictL1[i] == best:
                return (i, best, type(i))
    else:
        return False
            
    
# SANDBOX EXTRA PROBLEMS
# Problem 4

# Implement a function called closest_power that meets the specifications below. 

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exp = 0
    result = base ** exp
    if result == num:
        return exp
    else:
        while result <= num:
            exp += 1
            result = base ** exp
            #print(exp)
    if abs(num - result) >= abs(num - base**(exp-1)):
        return exp-1
    else:
        return exp
    
    
# Problem 5
# Write a Python function that returns the sum of the pairwise products of listA and listB. 
# You should assume that listA and listB have the same length and are two lists of integer numbers. 
# For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, 
# meaning your function should return: 32    
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    assert len(listA) == len(listB), 'Lists are of different leghts'
    if len(listA) == 0:
        return 0
    product = 0  
    for i in range(len(listA)):
        product += listA[i]*listB[i] 
    return product
    
# Problem 6
# Implement a function that meets the specifications below.
# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) 
# mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here 
    for i in L:
        i.reverse()
    L.reverse()
    
    
# Problem 7
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    intersect = {}
    difference = {}
    for key in d1:
        if key in d2:
            intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d1[key]
    for key in d2:
        if key not in d1:
            difference[key] = d2[key]
    return (intersect, difference)
    
    
# Problem 8
# Implement a function that meets the specifications below.    
    
def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here (best - github)
    newL = []
    for i in L:
        if g(f(i)) == True:
            newL.append(i)
    L[:] = newL
    if len(L) == 0:
        return -1
    else:
        return max(L)
        
                
    # Your code here (mine - 0.9/1)
    remove = []
    for i in L:
        if g(f(i)) == False:
            remove.append(i)
    for i in remove:
        L.remove(i)
    if len(L) == 0:
        return -1
    else:
        return(max(L))
        
# Problem 9
# Write a function to flatten a list. The list contains other lists, strings, or ints. 
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
        
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flatList = []
    for elm in aList:
        if type(elm) != list:
            flatList.append(elm)
        else:
            flatList.extend(flatten(elm))        
    return(flatList)
    
    
# Real exam
    
# Problem 3
# Write a simple procedure, myLog(x, b), that computes the logarithm of a 
# number x relative to a base b. For example, if x = 16 and b = 2, then the result is 4 
# - because 2^4=16. If x = 15 and b = 3, then the result is 2 - because 3^2 is the 
# largest power of 3 less than 15. In other words, myLog should return the largest 
# power of b such that b to that power is still less than or equal to x.
# x and b are both positive integers; b is an integer greater than or equal to 2. 
# Your function should return an integer answer.
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    logarithm = 0
    while b**(logarithm+1) <= x:
        logarithm += 1
    return logarithm
    
# Problem 5
# Write a Python function that returns a list of keys in aDict that map to integer values
# that are unique (i.e. values appear exactly once in aDict). The list of keys you return 
# should be sorted in increasing order. (If aDict does not contain any unique values, you 
# should return an empty list.)
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    unique = []
    values = list(aDict.values())
    for i in aDict:
        if values.count(aDict[i]) == 1:
            unique.append(i)
    return sorted(unique)
        
    