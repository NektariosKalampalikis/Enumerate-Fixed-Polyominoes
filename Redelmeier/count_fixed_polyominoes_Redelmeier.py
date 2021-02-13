import pprint #optional library


#Python implementation of : D. Hugh Redelmeier, 1981. Counting Polyominoes: Yet Another Attack, Discrete Mathematics 36, 191-203
#Expotential Complexity


def Neighbors(p,u,v): #check if node v is a neighbor of u , but v is untried
    for i in p:
        if i==u:
            continue
        upper=(i[0] ,i[1]+1 )
        down=(i[0] ,i[1]-1 )
        right=(i[0]+1 ,i[1] )
        left=(i[0]-1 ,i[1] )
        if right==v or upper==v or down==v or left==v:
            return True
    return False

def CountFixedPolyominoes(G,untried,n,p): #Redelmeier's algorithm
    global c 
    untried=list(untried)
    while len(untried)>0:
        u=untried[0]
        p.append(u)
        untried.remove(u)
        if len(p)==n:
            c=c+1
        else:
            new_neighbors=[]
            for v in G[u]: 
                if (v not in untried) and (v not in p)  and (not Neighbors(p,u,v)):
                    new_neighbors.append(v)
            new_untried=untried+new_neighbors 
            CountFixedPolyominoes(G,new_untried,n,p)
        p.remove(u)

#create the polyomino graph
def PolyominoGraph(n): #square lattice for : {(x,y)|(y>0) or (y=0) and x>=0}
    #form of coordinates: [y,x]
    polyominograph={}
    limit=n-2
    #bottom line,half line
    for y in range(0,n):
        polyominograph[(y,0)]=[]
    #all other lines,full lines
    for x in range(1,n):
        for y in range(-limit,limit+1):
            polyominograph[(y,x)]=[]
        limit+=-1 
    for i in polyominograph:
        upper=(i[0] ,i[1]+1 )
        down=(i[0] ,i[1]-1 )
        right=(i[0]+1 ,i[1] )
        left=(i[0]-1 ,i[1] )
        if right in polyominograph:
            polyominograph[i].append(right) 
        if upper in polyominograph:
            polyominograph[i].append(upper)
        if left in polyominograph:
            polyominograph[i].append(left)
        if down in polyominograph:
            polyominograph[i].append(down)
    return polyominograph 


#Python implementation of : D. Hugh Redelmeier, 1981. Counting Polyominoes: Yet Another Attack, Discrete Mathematics 36, 191-203
#Expotential Complexity 

#n=size of polyominoes
#p=current polyomino
#c=polyomino counter
#untried= an untried set of nodes

if __name__=="__main__":
    n=int(input("Size of polyomino:"))
    G=PolyominoGraph(n)
    untried={(0,0)}
    p=[]
    c=0
    printswitch=input("Do you want to pretty print the graph?(y/n):")
    if printswitch=="y" or printswitch=="yes":
        pprint.pprint(G)
    CountFixedPolyominoes(G,untried,n,p)
    print(c)

