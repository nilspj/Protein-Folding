import numpy as np
import random

#lager et grid med polymer av lengde N
#liten n er dimensjonen av matrisen
def startGrid(n,N):
    grid = np.zeros ((n,n)). astype(np.int16)
    polymer = np.linspace (1,N,N). astype(np.int16)
    for i in range(N):
        grid[int(np.round(n/2)), int(np.round(n/2-N/2))+i] = polymer[i]
    return grid

#printer grid 
def printGrid(grid):
    for i in range(grid.shape[0]):
        print("[", end="  ")
        for j in range(grid.shape[0]):
            print(grid[i][j], end="  ")
        print("]")
'''
def isLegalTwist (grid ,val, clockwise): 
    y,x = np.where(grid == val)
    for i in range(int(grid.shape[0])):
        if(clockwise==True):
            if(grid[x,y-i]==0):
                return True
            elif(grid[x+i,y]==0):
                return True
            else:
                return False
        elif(clockwise==False):
            if(grid[x,y+i]==0):
                return True
            elif(grid[x-i,y]==0):
                return True
            else:
                return False
    '''

#g1 = startGrid(20,9)

#printGrid(g1) #printer grid uten forandringer
'''
def twist(grid ,val, clockwise):
    N = grid.max()
    y,x = np.where(grid == val)#Koordinater til value
    midPoint = int(N/2)+1 
    my,mx = np.where(grid == midPoint)#koordinater til midPoint
    mainSide = random.randint(0,1)#Bestemmer hvilken side av midtpunkt som skal rotere 
    if((x>mx)):#Rot punkt til høyre for midtpunkt
        rigMat = deepcopy(grid)
        rotMat = deepcopy(grid)
        rigMat[rigMat>=val]=0
        rotMat[rotMat<val]=0
        part=rotMat[(int(y)-(N-val)):(int(y)+N-val+1),(int(x)-(N-val)):(int(x)+N-val+1)]
        if(clockwise==True):#sjekker om det skal roteres mot eller med klokka
            part=np.rot90(part)
        elif(clockwise==False):
            part=np.rot90(part, axes=(0,1))
        rotMat[(int(y)-(N-val)):(int(y)+N-val+1),(int(x)-(N-val)):(int(x)+N-val+1)]=part
        grid = rigMat + rotMat
        return grid
        
    elif((x<mx)):#rot punkt til venstre for midtpunkt
        rigMat = deepcopy(grid)
        rotMat = deepcopy(grid)
        rigMat[rigMat<=val]=0
        rotMat[rotMat>val]=0
        part=rotMat[(int(y)-val):(int(y)+val+1),(int(x)-val):(int(x)+val+1)]
        if(clockwise==True):#sjekker om det skal roteres mot eller med klokka
            part=np.rot90(part)
        elif(clockwise==False):
            part=np.rot90(part, axes=(1,0))
        rotMat[(int(y)-val):(int(y)+val+1),(int(x)-val):(int(x)+val+1)]=part
        grid = rigMat + rotMat
        return grid

    elif (x==mx) and (mainSide == 1):#midtpunkt valgt som rot punkt, roterer venstre side
        rigMat = deepcopy(grid)
        rotMat = deepcopy(grid)
        rigMat[rigMat<=val]=0
        rotMat[rotMat>val]=0
        part=rotMat[(int(y)-val):(int(y)+val+1),(int(x)-val):(int(x)+val+1)]
        if(clockwise==True):#sjekker om det skal roteres mot eller med klokka
            part=np.rot90(part)
        elif(clockwise==False):
            part=np.rot90(part, axes=(1,0))
        rotMat[(int(y)-val):(int(y)+val+1),(int(x)-val):(int(x)+val+1)]=part
        #Får error her av og til: 
        #ValueError: could not broadcast input array from shape (15,0) into shape (0,15)
        grid = rigMat + rotMat
        return grid
    
    elif (x==mx) and (mainSide == 0):#midtpunkt valgt som rot punkt, roterer høyre side
        rigMat = deepcopy(grid)
        rotMat = deepcopy(grid)
        rigMat[rigMat>=val]=0
        rotMat[rotMat<val]=0
        part=rotMat[(int(y)-(N-val)):(int(y)+N-val+1),(int(x)-(N-val)):(int(x)+N-val+1)]
        if(clockwise==True): #sjekker om det skal roteres mot eller med klokka
            part=np.rot90(part)
        elif(clockwise==False):
            part=np.rot90(part, axes=(0,1))
        rotMat[(int(y)-(N-val)):(int(y)+N-val+1),(int(x)-(N-val)):(int(x)+N-val+1)]=part
        grid = rigMat + rotMat
        return grid
'''
# test , midtpoint = 5
g1=startGrid(15,9)

printGrid(g1)
g2 = startGrid(36,30)
print(g2)
#printGrid(twist(g1,6,9)) 
#################################################################################################

#To do list!!!!
#må få fikset error i linje 86
#må få twist til å sjekke for y koordinater også
#må implementere en isLegalTwist funksjon for å unngå at reglene blir brudt i twist
#Lage en funksjon som twister random 
#Organisere funksjonene i common

    
    
    
    
    
    
    
    
    
    
