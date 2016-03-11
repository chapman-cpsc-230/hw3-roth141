# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 18:13:12 2016

@author: LydiaRoth
"""

import turtle
bob= turtle.Pen()

num_sidesinp= raw_input ("Enter number of sides:")
num_sides = int(num_sidesinp)
lengthinp = raw_input ("Enter natural number length:")
length = int(lengthinp)

for side in range(num_sides): 
 
        bob.forward(length)
        bob.left(180-180.0/num_sides)
   

    
inp = raw_input("hit <enter> to quit")   
turtle. bye()   