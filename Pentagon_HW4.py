# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 23:22:45 2016

@author: LydiaRoth
"""

import turtle
bob= turtle.Pen()
bob.left(35) ### MAM: What's this for?
num_sidesinp= raw_input ("Enter number of sides:")
num_sides = int(num_sidesinp)
length = raw_input ("Enter length:") ## You never use this user input. 
                                     ## So if the user asked for a bigger figure, 
                                     ### it would still use 100


for side in range(num_sides): 
     bob.forward(100.0)
     bob.right(360.0/num_sides)
   
     
    
inp = raw_input("hit <enter> to quit")   
turtle. bye()   
