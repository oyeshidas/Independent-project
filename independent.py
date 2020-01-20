# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:16:11 2020

@author: gy19ynk
"""

import numpy as np
import matplotlib.pyplot


#Reads the file 'drunk.plan.txt'
Field = np.genfromtxt("drunk.plan.txt", delimiter= ',')


f = open('drunk.plan.txt')
environment = []
for row in f:
    parsed_row = str.split(row, ",")
    rowlist=[]
    for value in parsed_row:
            rowlist.append(float(value))
    environment.append(rowlist)
f.close()
for a in range (300):
    for b in range (300):
        if environment[a][b] == 1:
            environment[a][b]= 100

matplotlib.pyplot.imshow(environment) #plots environment
matplotlib.pyplot.show














