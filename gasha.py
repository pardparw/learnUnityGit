import math
a = int(input())
b = int(input())
OreS = 1
Ma = 10

OreN = 1
MN = 10
index = 1

ob = 0
mb = 0
of = 0
mf = 0
mmmmm = a
ooooo = b
for i in range(30):
    
    ob = OreN
    mb = MN
    mmmmm = Ma
    ooooo = OreS
    print(f"M:{MN} __ {Ma}, O: {OreN} __ {OreS} ==== {index}")
    OreS += OreN
    Ma += MN
    
    MN = math.ceil(MN + (MN/2))
    OreN = OreN * 2    
    
    of = OreN
    mf = MN    
    #print(f"{a-mb <= 0 },{ b-ob <= 0 } ,{a-mf <= 0 },{ b-of <= 0}")
    
    if(a-mb <= 0 or b-ob <= 0 or a-mf <= 0 or b-of <= 0):
        #mmmmm -= mb
        #ooooo -= ob
        
        if((a-mf > -1) and (b-of > -1)):
            mmmmm -= mf
            ooooo -= of
            index +=1
            print(f"M:{MN} __ {Ma}, O: {OreN} __ {OreS} ==== {index} rrrr")

        print(f"Level 1 -> {index}")
        print(f"Money: {a -  mmmmm} Popo")
        print(f"Magic Ore: {b - ooooo}")
        break
    
    index += 1
        
        
                
        
    
    
   
