# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:37:40 2017

@author: Vsevold Loik
"""

# Problem 3
# Implement a function that meets the specifications below.

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    mysum = 0
    errors = 0
    for i in s:
        try:
            mysum += int(i)
        except ValueError:
            errors += 1
    if errors == len(s):
        raise ValueError
    else:
        return mysum
            
            
# Problem 4
# Implement a function that meets the specifications below.

def max_val(t): 
    """ t, tuple 
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    def flatten(aList):
        flatList = []
        for elm in aList:
            if type(elm) != int:
                flatList.extend(flatten(elm)) 
            else:
                flatList.append(elm)       
        return(flatList)
    
    flat = flatten(t)
    return max(flat)
    
# Problem 5
# Implement a function that meets the specifications below.
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    dictionary = {}
    decoded = ''
    for i in range(len(map_from)):
        dictionary[map_from[i]] = map_to[i]
    for j in code:
        decoded += dictionary[j]
    return (dictionary, decoded)
       
       
# Problem 6
# Problem 6-1
        
# You are given the following superclass. Do not modify this.
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
        
# Write a class that implements the specifications below. Do not override any methods of Container.
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs one or more times in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        try:
            self.vals[e] -= 1
        except:
            pass                        
            
    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        try:
            return self.vals[e]
        except KeyError:
            return 0
            
    def __add__(self, other):
        union = Bag()
        for i in self.vals:
            for j in range(self.count(i)):
                union.insert(i)
        for i in other.vals:
            for j in range(other.count(i)):
                union.insert(i)
        return union
        
        
# Problem 6-3
# Write a class that implements the specifications below. Do not override any methods of Container.
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        try:
            del self.vals[e]
        except KeyError:
            pass
        
    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here   
        if e in self.vals:
            return True
        else:
            return False
            
# Problem 7
You are given the following two classes.
### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
        
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    #nextID = 0
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        self.tents = [tent_loc]
        #self.tentID = MITCampus.nextID
        #MITCampus.nextID += 1
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        self.new_tent_loc = new_tent_loc
        if all(self.new_tent_loc.dist_from(i) >= 0.5 for i in self.tents):
            #self.tentID = MITCampus.nextID
            self.tents.append(new_tent_loc)
            return True
        else:
            return False
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if tent_loc in self.tents:       
            self.tents.remove(tent_loc)
        else:
            raise ValueError
        
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        for i in range(len(self.tents) - 1):
            j=i+1
            while j < len(self.tents):
                if self.tents[i].getX() > self.tents[j].getX():
                   temp = self.tents[i]
                   self.tents[i] = self.tents[j]
                   self.tents[j] = temp
                j += 1
        self.new= []        
        for i in self.tents:
            self.new.append(str(i))       
        return self.new
        
# Real exam

# Problem 3
def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    flag = True
    for i in range(len(aString)):
        if aString[i] == aString[len(aString)-1-i]:
            flag = True
        else:
            flag = False
            break
    return(flag)