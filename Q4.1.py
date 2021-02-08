# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 17:19:21 2018

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
twists = np.linspace(1,dmax,dmax)

#Eplot = np.zeros(dmax)

#Do this fifty times
def recurringgrid(grid,h):
    Eplot = np.zeros(dmax)
    x = 0
    y = 49
    Evec = co.legalEnergyGrid(grid,d,N,U,tempScale[y])[0]
    copygrid = co.legalEnergyGrid(grid,d,N,U,tempScale[y])[2]
    for i in range(0,d):
        Eplot[i] = Evec[i]
    print(Evec)
    print(Eplot)
    while True:
        x +=1
        y -=1
        Evec = co.legalEnergyGrid(copygrid,d,N,U,tempScale[y])[0]
        copygrid = co.legalEnergyGrid(copygrid,d,N,U,tempScale[y])[2]
        print(Evec)
        for j in range(d*x,d+d*x):
            Eplot[j] = Evec[j-d*x]
        print(Eplot)
        if x == h-1:
            break
    return Eplot

#Eplot2 = recurringgrid(poly15,50)
Eplot2 = recurringgrid(poly30,50)
#print(Eplot2)

twiststep = np.linspace(1,dmax,50)
'''
Estep = np.zeros(50)
for i in range(0,50):
    Estep[i] = Eplot2[i*d]
'''
'''
eVec = co.legalEnergyGrid(poly15,d,N,U,T)[0]
copygrid = co.legalEnergyGrid(poly15,d,N,U,T)[2]
Eplot0 = eVec

eVec1 = co.legalEnergyGrid(copygrid,d,N,U,T-30)[0]
copygrid1 = co.legalEnergyGrid(copygrid,d,N,U,T-30)[2]
Eplot1 = eVec1

print(Eplot0)
print(Eplot1)
Eplot = np.zeros(2*d)
for i in range(0,d):
    Eplot[i] = Eplot0[i]

for i in range(d,2*d):
    Eplot[i] = Eplot1[i-d]
    
print(Eplot)
'''

#plt.plot(twiststep,Estep,'rx',linewidth=0.5,markersize=6,label='Temperature drop')
for xc in twiststep:
    if xc == 1:
        plt.axvline(x=xc,color='r',linewidth=0.5,label='Temperature drop')
    else:
        plt.axvline(x=xc,color='r',linewidth=0.5)

plt.plot(twists,Eplot2,linewidth=0.15,label='E')
plt.xlabel('Twists'+r"$\,[\mathrm{1}]$", fontsize=14)
plt.ylabel('Energy'+r"$\,[\mathrm{J}]$",fontsize=14)
plt.xlim(1,dmax)
plt.legend(loc=1,fontsize=14)
plt.figure()
