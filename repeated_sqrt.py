# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:52:06 2016

@author: LydiaRoth
"""

from math import sqrt
for n in range(1,60):
    r = 2.0
for i in range(n):
    r = sqrt(r)
for i in range(n):
    r = r**2
print '%d times sqrt and **2: %.16f' % (n,r)



from math import sqrt
for n in range(1,25):
    r = 2.0
for i in range(n):
    r = sqrt(r)
for i in range(n):
    r = r**2
print '%d times sqrt and **2: %.2f' % (n,r)
#This program takes a value(2) and computes the square root than multiplies the product  
# of the sqaure root by the product of the value(2) squared. 

# We come back to 1 and not 2 becuase we are completing inverse mathematical operations on 
# R and looping 59 times which creates round off error. 