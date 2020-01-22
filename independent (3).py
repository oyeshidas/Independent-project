# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:16:11 2020

@author: gy19ynk
"""

import numpy as np
import matplotlib.pyplot
import agentframework
import matplotlib.animation
#import tkinter


num_of_drunks = 25
drunks =[]
house = 25
pub=1
start_coor=[]

#Reads the file 'drunk.plan.txt'
Field = np.genfromtxt("drunk.plan.txt", delimiter= ',')

#displays the pubs and homes on screen
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


for i in range (num_of_drunks):
    drunks.append(agentframework.drunks(drunks,house, environment))
    
       
for i in range (num_of_drunks):    
    house = (i+1)*10
    drunks.append(agentframework.drunks(drunks, house, environment))
    

    matplotlib.pyplot.imshow(environment) #plots environment
matplotlib.pyplot.show


for i in range(num_of_drunks):
    #creates scatter plot of the list of agents
    matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y) 
    matplotlib.pyplot.draw()   # show environment 
    
    carry_on = True	
  
def distance_between(self, drunks):
    return (((self.x - drunks.x)**2) + ((self.y - drunks.y)**2))**0.5
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
while num_of_drunks>0:
     house+=1
     num_of_drunks-=1


def update(frame_number):
    
    fig.clear()
    
    
    
    for j in range(num_of_steps):
        for i in range(num_of_drunks):
            drunks[i].move()
            drunks[i].add()
    
    matplotlib.pyplot.xlim(0,300)  #plots x values
    matplotlib.pyplot.ylim(0,300) #plots y values
    matplotlib.pyplot.imshow(environment) #plots environment
    
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_steps) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
    
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
    

    
#root = tkinter.Tk() #main python window
#root.wm_title("independent!!")
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#simple event based programming model
#menu_bar = tkinter.Menu(root)
#root.config(menu=menu_bar)
#model_menu = tkinter.Menu(menu_bar)
#menu_bar.add_cascade(label="independent", menu=model_menu)
#model_menu.add_command(label="Run model", command=run)
    
    
    








          
  

#returns the function so that it is resumable		
#def gen_function(b = [0]):
    #a = 0
    #global carry_on 
    #while (a < num_of_iterations) & (carry_on) :
        #yield a			# Returns control and waits next call.
        #a = a + 1








