# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:24:56 2019

@author: 44781

"""

#builds agents class, initialises them in a random location,and moves them
import random
class drunks:
    
    def __init__(self,drunks , house, environment): #initialises the agents and their environment
        self.drunks = drunks
        self.environment=environment
        self.house = house
        

    
class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self.x = random.randint(149,150)
        self.y = random.randint(150,151)
    def move(self): #moves the individual agents
        
        if random.random() < 0.5:
            self.x= (self.x+1)% 300
        else :
            self.x=(self.x-1)%300
        
        if random.random() < 0.5:
             self.y= (self.y+1) % 300
        else :
            self.y=(self.y-1) %300 
            
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    

          




