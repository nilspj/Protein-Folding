# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:31:32 2018

@author: threl300697
"""

import numpy as np
import common as co
import matplotlib.pyplot as plt

T1 = 0.001
N = 15
poly15 = co.startGrid(21,15)

U = np.zeros((N+2,N+2))
for i in range (1,N+1):
    for j in range (1,N+1):
        if(i==j)or(i==j+1)or(j==i+1):
            U[i,j]==0
        else:
            U[i,j] = np.random.uniform(-10.4*10**(-21),-3.47*10**(-21))
U = np.triu(U) + np.rot90(np.flip(np.triu(U),1),5)

xVec =np.linspace(0,10,10)
meanE0 = np.zeros(len(xVec))
for i in range (0,len(xVec)):
    print(i)
    eVec = co.legalEnergyGrid(poly15,co.dFunc(T1),N,U,T1)[0]
    meanE0[i]= np.mean(eVec)
print(meanE0)

plt.plot(xVec,meanE0,'r',label=r"$\langle E \rangle$")
plt.ylabel('Energy'+r"$\,[\mathrm{J}]$", fontsize=13)
plt.xlabel('N'+r"$\,[\mathrm{1}]$", fontsize=14)
plt.xlim(0,10)
plt.legend(loc=1,fontsize=14)
plt.figure()