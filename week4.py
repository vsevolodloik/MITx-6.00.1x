# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:55:00 2016

@author: Vsevolod Loik
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   try:
       return item / denom
   except ZeroDivisionError:
       return 0
   