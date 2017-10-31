# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:42:00 2016

@author: Vsevolod Loik
"""

# Finger exercises
varA = 2
varB = 4
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else: 
    print('smaller')
#######################################################

count = 2
while count <= 10:
    print(count)
    count += 2
print('Goodbye!')
#######################################################

count = 10
print('Hello!')
while count >= 2:
    print(count)
    count -= 2
#######################################################

end = 6
mysum = 0
count = 1
while count <= end:
    mysum = mysum + count
    print(mysum)    
    count += 1
print(mysum)
####################################################### 

for i in range(2,11,2):
    print(i)
print("Goodbye!")
#######################################################

print("Hello!")
for i in range(10,0,-2):
    print(i)
#######################################################

end = 6
mysum = 0
for i in range(1,end+1):
    mysum = mysum + i
    print(mysum)
print(mysum)

