import numpy as np
import common as co
import matplotlib.pyplot as plt 

T1 = 0.001
T2 = 500
dmax = 5000 
N = 15

U = np.zeros((N+2,N+2))
for i in range (1,N+1):
    for j in range (1,N+1):
        if(i==j)or(i==j+1)or(j==i+1):
            U[i,j]==0
        else:
            U[i,j] = np.random.uniform(-10.4*10**(-21),-3.47*10**(-21))
U = np.triu(U) + np.rot90(np.flip(np.triu(U),1),5)

poly15 = co.startGrid(21,15)

twists = np.linspace(1,dmax,dmax)
#print(twists)
eVec = co.legalEnergyGrid(poly15,5000,N,U,T1)[0]

print(eVec)
plt.plot(twists,eVec,'r',linewidth=1.5,label='E')
plt.ylabel('Energy'+r"$\,[\mathrm{J}]$", fontsize=13)
plt.xlabel('Twists'+r"$\,[\mathrm{1}]$", fontsize=14)
plt.xlim(0,5000)
plt.legend(loc=1,fontsize=14)
plt.figure()