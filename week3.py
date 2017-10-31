# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:42:48 2016

@author: Vsevolod Loik
"""
# Finger Exercises
test = ('I', 'am', 'a', 'test', 'tuple')
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    t = ()    
    for i in range(len(aTup)):
        if i%2 == 0:   # odd - 1,3,5... but as indexing in python starts with zero, we seek for indexes 0,2,4...
            t = t + (aTup[i],)
    return t
    # simple alternative - slising
    # return aTup[::2]

############################################################################## 
# absolute value
testList = [1, -4, 8, -9]

def absoluteValue(list):
    for i in range(len(list)):
        list[i] = abs(list[i])
    return list
 
##############################################################################    
# animals in the dictionary
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
def how_many(aDict):
    mysum = 0
    for letters in aDict:
        mysum += len(aDict[letters])
    return mysum
    
##############################################################################     
def biggest(aDict):
    best = 0
    for key in aDict:
        if len(aDict[key]) > best:
            best = len(aDict[key])
    for key in aDict:
        if len(aDict[key]) == best:
            return key
    
##############################################################################     
def biggest(aDict):                         #alternative solution
    biggest_value = 0
    result = None
    for key in aDict:                       # or aDict.keys()
        if len(aDict[key]) > biggest_value:
            result = key
            biggest_value = len(aDict[key])
    return result
    
    
    
    
   