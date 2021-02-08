# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 11:18:40 2018

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
def recurringEgrid(grid,h):
    Emean = np.zeros(h)
    x = 0
    y = 49
    Evec = co.legalEnergyGrid(grid,d,N,U,tempScale[y])[0]
    copygrid = co.legalEnergyGrid(grid,d,N,U,tempScale[y])[2]
    Emean[0] = np.mean(Evec)
    print(Evec)
    print(Emean)
    while True:
        x +=1
        y -=1
        Evec = co.legalEnergyGrid(copygrid,d,N,U,tempScale[y])[0]
        copygrid = co.legalEnergyGrid(copygrid,d,N,U,tempScale[y])[2]
        Emean[x] = np.mean(Evec)
        print(Evec)
        print(Emean)
        if x == h-1:
            break
    return Emean

Emean2 = recurringEgrid(poly30,50)
tempScale1=np.linspace(1500.01,0.01,50)

plt.plot(tempScale1,Emean2,'r',linewidth=1,label=r"$\langle E \rangle$")
plt.ylabel('Energy'+r"$\,[\mathrm{J}]$", fontsize=13)
plt.xlabel('Temperature'+r"$\,[\mathrm{K}]$", fontsize=14)
plt.xlim(1500,0)
plt.legend(loc=1,fontsize=14)
plt.figure()