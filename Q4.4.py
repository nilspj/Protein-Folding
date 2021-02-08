# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:30:53 2018

@author: threl300697
"""

import numpy as np
import common as co
import matplotlib.pyplot as plt 

#N = 15
N = 30
d = 600
poly15 = co.startGrid(21,15)
poly30 = co.startGrid(36,30)
dmax = 30000
T = 1500

U = np.zeros((N+2,N+2))
for i in range (1,N+1):
    for j in range (1,N+1):
        if(i==j)or(i==j+1)or(j==i+1):
            U[i,j]==0
        else:
            U[i,j] = np.random.uniform(-10.4*10**(-21),-3.47*10**(-21))
U = np.triu(U) + np.rot90(np.flip(np.triu(U),1),5)

tempScale=np.linspace(0.01,1500.01,50)

#Eplot = np.zeros(dmax)

#Do this fifty times
def recurringPolymerGrid(grid,h):
    x = 0
    y = 49
    copygrid = co.legalEnergyGrid(grid,d,N,U,tempScale[y])[2]
    print(tempScale[y])
    #print(copygrid)
    while True:
        x +=1
        y -=1
        copygrid = co.legalEnergyGrid(copygrid,d,N,U,tempScale[y])[2]
        print(tempScale[y])
        #print(copygrid)
        if x == h-1:
            break
    return copygrid

copygrid1 = recurringPolymerGrid(poly30,50)
#copygrid2 = recurringPolymerGrid(poly15,50)

def getPosList(grid):
    yList=[]
    xList=[]
    for i in range(1,31):
        yList.append(np.where(grid == i)[0])
        xList.append(np.where(grid == i)[1])
    return xList,yList


plt.plot(getPosList(copygrid1)[0],getPosList(copygrid1)[1],'ro-')
#plt.plot(getPosList(copygrid2)[0],getPosList(copygrid2)[1],'gx-')
plt.figure()
