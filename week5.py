# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 14:17:55 2017

@author: Vsevolod Loik
"""
# Exercise: coordinate

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False
            
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'        
    
# Exercise: int set
    
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self, other):
        """returns a new intSet of integers that appear in both s1 and s2"""
        inter = intSet()        
        for i in self.vals:
            if i in other.vals:
                inter.insert(i)
        return inter
        
    def __len__(self):
        """Returns length of s"""
        count = 0
        for i in self.vals:
            count += 1
        return count               
        
        
# TEST
a = intSet()
a.insert(3)
a.insert(5)
a.insert(7)        
        
        
# Exercise: genPrimes     
# Write a generator, genPrimes, that returns the sequence of prime numbers 
# on successive calls to its next() method: 2, 3, 5, 7, 11, ...
# Have the generator keep a list of the primes it's generated. 
# A candidate number x is prime if (x % p) != 0 for all earlier primes p.
def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next



       
def genPrimes():
    primes = [2]
    cand = 3
    while True:        
        if all((cand % p) != 0 for p in primes):
            yield primes[-1]
            primes += [cand]
            cand += 1
        else:
            cand += 1
            
def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last            
        
      
    
    
    