import numpy as np
import common as co
import matplotlib.pyplot as plt 

#N = 15
N = 30
d=10 # Eller co.dFunc(T)
poly15 = co.startGrid(21,15)
poly30 = co.startGrid(36,30)

U = np.zeros((N+2,N+2))
for i in range (1,N+1):
    for j in range (1,N+1):
        if(i==j)or(i==j+1)or(j==i+1):
            U[i,j]==0
        else:
            U[i,j] = np.random.uniform(-10.4*10**(-21),-3.47*10**(-21))
U = np.triu(U) + np.rot90(np.flip(np.triu(U),1),5)

def diameter(grid,n):
    posx=np.zeros(n)
    posy=np.zeros(n)
    for i in range(1,n+1):
        y,x = np.where(grid==i)
        posx[i-1]=x
        posy[i-1]=y
    Ly = np.max(posy)-np.min(posy)+1
    Lx = np.max(posx)-np.min(posx)+1
    return max(Lx,Ly)

'''
poly15 = co.twistfunc(poly15)
poly15 = co.twistfunc(poly15)
poly15 = co.twistfunc(poly15)
poly15 = co.twistfunc(poly15)
co.printGrid(poly15)
print(diameter(poly15,N))
'''
tempScale=np.linspace(0.01,1500.01,50)
meanLVec = np.zeros(len(tempScale))
for temp in range (0,len(tempScale)):
    print(temp)
    #eVec = np.zeros(int(co.dFunc(tempScale[temp])))
    #for i in range(1,int(co.dFunc(tempScale[temp]))+1):
        #print(i)
    LVec = co.legalEnergyGrid(poly30,co.dFunc(tempScale[temp]),N,U,tempScale[temp])[1]
    meanLVec[temp]= np.mean(LVec)
print(meanLVec)

'''
tempScale=np.linspace(0.01,1500.01,10)
print(len(tempScale))
lengthVec=np.zeros(len(tempScale))
for i in range(len(tempScale)):
    print(i)
    lengthVec[i] = diameter(co.legalEnergyGrid(poly15,co.dFunc(tempScale[i]),N,U,tempScale[i])[1],N)
'''
plt.plot(tempScale,meanLVec,'g',label=r"$\langle L \rangle$")
plt.ylabel('Diameter'+r"$\,[\mathrm{1}]$", fontsize=13)
plt.xlabel('Temperature'+r"$\,[\mathrm{K}]$", fontsize=14)
plt.xlim(0,1500)
plt.legend(loc=4,fontsize=14)
plt.figure()
#plt.savefig('Question 3.pdf')