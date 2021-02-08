import common as co
import numpy as np 
import matplotlib.pyplot as plt 


g1= co.startGrid(15,10)
#co.printGrid(g1)

g2= co.startGrid(15,10)
g2= co.twistfunc(g2)
#co.printGrid(g2)

g3= co.startGrid(15,10)
g3=co.twistfunc(g3)
g3=co.twistfunc(g3)
#co.printGrid(g3)

g4 = co.startGrid(36,30)
g4=co.twistfunc(g4)
g4=co.twistfunc(g4)

def getPosList(grid):
    yList=[]
    xList=[]
    for i in range(1,31):
        yList.append(np.where(grid == i)[0])
        xList.append(np.where(grid == i)[1])
    return xList,yList


#plt.plot(getPosList(g1)[0],getPosList(g1)[1],'ro-')
#plt.plot(getPosList(g2)[0],getPosList(g2)[1],'rx-', markersize=8)
#plt.plot(getPosList(g3)[0],getPosList(g3)[1],'r*-', markersize=8)
plt.plot(getPosList(g4)[0],getPosList(g4)[1],'r*-', markersize=8)
#plt.xlim(0,14)
#plt.ylim(0,14)
plt.figure()