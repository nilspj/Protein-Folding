import numpy as np

kb=1.380649*10**(-23) #Boltzmanns konstant


#lager et grid med polymer av lengde N
#liten n er dimensjonen av matrisen

def startGrid(n,N):
    grid = np.zeros ((n,n)). astype(np.int16)
    polymer = np.linspace (1,N,N). astype(np.int16)
    for i in range(N):
        grid[int(np.round(n/2)), int(np.round(n/2-N/2))+i] = polymer[i]
    return grid

def printGrid(grid):
    for i in range(grid.shape[0]):
        print("[", end="  ")
        for j in range(grid.shape[0]):
            print(grid[i][j], end="  ")
        print("]")

def twistfunc(grid):
    '''finn midpunkt
    finn ut om verdi er større eller mindre enn midpunkt
    hvis større, twist alle de større enn verdi
    hvis mindre, twist alle mindre enn verdi'''
 
    while True:
        clockwise = np.random.choice([1,-1])
        R = clockwise*np.matrix("0 -1 ; 1 0")
        copygrid = np.copy(grid)
        N = copygrid.max()
        val = np.random.randint(2,N-1)
        p0 = np.where(copygrid == val)#Koordinater til value
        p0 = np.matrix(p0)
        midPoint = int(N/2)+1
        coinFlip = np.random.randint(0,1)
        if val > midPoint:
            for i in range(val+1,N+1):
                pI = np.where(grid == i)
                pI = np.matrix(pI)
                newpoint = p0 + np.matmul(R,pI - p0)
                copygrid[newpoint[0],newpoint[1]] = copygrid[pI[0],pI[1]]
                copygrid[pI[0],pI[1]] = 0
                #print(pI)
                #print(newpoint)
        elif val < midPoint:
            for i in range(1,val):
                pI = np.where(grid == i)
                pI = np.matrix(pI)
                newpoint = p0 + np.matmul(R,pI - p0)
                copygrid[newpoint[0],newpoint[1]] = copygrid[pI[0],pI[1]]
                copygrid[pI[0],pI[1]] = 0
        elif val == midPoint:
            start =[1,val+1]
            end = [val,N+1]
            for i in range(start[coinFlip],end[coinFlip]):
                pI = np.where(grid == i)
                pI = np.matrix(pI)
                newpoint = p0 + np.matmul(R,pI - p0)
                copygrid[newpoint[0],newpoint[1]] = copygrid[pI[0],pI[1]]
                copygrid[pI[0],pI[1]] = 0
        nonzeros = np.count_nonzero(copygrid)
        if nonzeros == N:
            break
    return copygrid
##################################################
#Oppgave 2
def nearestNeighbours(grid,N,U,x,y):
    E = 0
    if x+1 < N:
        E = E + U[grid[x+1,y],grid[x,y]]
    if x-1 >= 0:
        E = E + U[grid[x-1,y],grid[x,y]]
    if y+1 < N:
        E = E + U[grid[x,y+1], grid[x,y]]
    if (y-1) >= 0:
        E = E + U[grid[x,y-1],grid[x,y]]
    return E

def calculateEnergy(grid,N,U):
# R et u r n s t h e t o t a l e n e r g y o f t h e g r i d
    E = 0
    for i in range(1,N):
        pos = np.argwhere(grid == i)[0]
        E = E + 0.5*nearestNeighbours(grid,N,U,pos[0],pos[1])
        # m u l t i p l y by 0 . 5 t o a v oi d d o u bl e c o u n t i n g
    return E

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

def legalEnergyGrid(grid,d,N,U,T):
    Enew = 0
    x = 0
    y = -1
    Evector = np.zeros(d)
    Lvector = np.zeros(d)
    while True:
        x += 1
        y +=1
        print(x,T)
        if x != d+1:
            E1 = calculateEnergy(grid,N,U)
            L1 = diameter(grid,N)
            copygrid = twistfunc(grid)
            Enew = calculateEnergy(copygrid,N,U)
            #print(Enew)
            Lnew = diameter(copygrid,N)
            #print(Lnew)
            if Enew < E1:
                grid = copygrid  
                Evector[y] = Enew
                Lvector[y] = Lnew
            elif np.random.uniform(0,1) < np.exp(-(Enew - E1)/(kb*T)):
                grid = copygrid
                Evector[y] = Enew
                Lvector[y] = Lnew
            else:
                Evector[y] = E1
                Lvector[y] = L1
            #np.append(Evector,Enew) 
            #np.append(Lvector,Lnew)
        elif x == d+1:
            break
    return Evector,Lvector,grid

def dFunc(T):
    #dmax = 11500
    #s = 7*10**(-4)
    #dmax = 15000
    #s = 0.0004
    dmax = 20000
    s = 0.001
    return int(dmax*np.exp(-s*T))

#################################################
'''
def multipleTwists(grid,d,N,U,T):
    x = 0
    while True:
        x += 1
        if x != d+1:
            #grid = legalEnergyGrid(grid,N,U,T)
        elif x == d+1:
            break
    return grid

N=15
U = np.zeros((N+2,N+2))
for i in range (1,N+1):
    for j in range (1,N+1):
        U[i,j] = np.random.uniform(-10.4*10**(-21),-3.47*10**(-21))
'''
#g1=startGrid(15,10)
#g1=twistfunc(g1) 
#g1=legalEnergyGrid(g1,10,N,U,5)
#print(g1)
