# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:35:28 2018

@author: threl300697
"""

import numpy as np
import common as co
import matplotlib.pyplot as plt

dmax = 11500
s = 7*10**(-4)
T = 0
d_T = dmax*np.exp(-s*T)
Tend = 1500
Nt = int(1500/10)
dt = Tend/Nt
N = 30
#N = 15
kb=1.380649*10**(-23) #Boltzmanns konstant


U = np.zeros((N+2,N+2))
for i in range (1,N+1):
    for j in range (1,N+1):
        if(i==j)or(i==j+1)or(j==i+1):
            U[i,j]==0
        else:
            U[i,j] = np.random.uniform(-10.4*10**(-21),-3.47*10**(-21))
U = np.triu(U) + np.rot90(np.flip(np.triu(U),1),5)
#co.printGrid(U)

poly15 = co.startGrid(21,15)
poly30 = co.startGrid(36,30)
    
'''
newE = legalEnergyGrid(poly15,dFunc(10),N,U,10)[1]
print(newE)
print(dFunc(10))
'''
tempScale=np.linspace(0.01,1500.01,50)
meanVec = np.zeros(len(tempScale))
for temp in range (0,len(tempScale)):
    print(temp)
    #eVec = np.zeros(int(co.dFunc(tempScale[temp])))
    #for i in range(1,int(co.dFunc(tempScale[temp]))+1):
        #print(i)
    eVec = co.legalEnergyGrid(poly30,co.dFunc(tempScale[temp]),N,U,tempScale[temp])[0]
    meanVec[temp]= np.mean(eVec)
print(meanVec)

plt.plot(tempScale,meanVec,'r',label=r"$\langle E \rangle$")
plt.ylabel('Energy'+r"$\,[\mathrm{J}]$", fontsize=13)
plt.xlabel('Temperature'+r"$\,[\mathrm{K}]$", fontsize=14)
plt.xlim(0,1500)
plt.legend(loc=4,fontsize=14)
plt.figure()
#plt.savefig('Question 2_1.pdf')
