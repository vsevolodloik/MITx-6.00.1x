# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:57:06 2017

@author: Vsevolod Loik
"""

# Problem Set 1

# Problem 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl'
s = 'azcbobobegghaklaaoi'
vowel = 0
for char in s:
    if char ==  'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
         vowel += 1
print('Number of vowels: ' + str(vowel))

# Problem 2
# find Bob
s = 'azcbobobegghaklaaoibobobob'
bob = 0
for i in range(0, len(s)):
    if s[i:i+3] == 'bob':
        bob += 1
print('Number of times bob occurs is: ' + str(bob))


# Problem 3
# longest string in alfabetical order
s = 'azcbobobegghakl'
ws = s[0]
bs = ws

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        ws += s[i+1]
    else:
        ws = s[i+1]
    if len(ws) > len(bs):
            bs = ws
print('Longest substring in alphabetical order is: ' + bs)