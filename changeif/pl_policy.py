import gurobipy as gb
from gurobipy import *
import numpy as np
def transfer(a):
    if a==0:
        return(-1,0)
    if a==1:
        return(1,0)
    if a==2:
        return(0,-1)
    if a==3:
        return(0,1)

def calculTransfert(grill,i,j,a,p):
    
    c=i+1
    d=j+1
    p1=(1+p)/2
    p2=(1-p)/2
    e,f=transfer(a)
    up,down,left,right,reset,upleft,upright,downleft,downright=0,0,0,0,0,0,0,0,0
    if a==0:#up
        if grill[c-1][d][0]==0 :
            reset=1
        if grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            down=1
        if grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            down=p1
        if grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            down=p1
        if grill[c][d-1][0]!=0 and grill[c][d+1][0]!=0:
            down= p
        if grill[c][d-1][0]!=0 :
            downleft=p2 
        if grill[c][d+1][0]!=0:           
            downright=p2 
    if a==1:#down
        if grill[c+1][d][0]==0 :
            reset=1
        if grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            up=1
        if grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            up=p1
        if grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            up=p1
        if grill[c][d-1][0]!=0 and grill[c][d+1][0]!=0:
            up= p
        if grill[c][d-1][0]!=0 :
            upleft=p2 
        if grill[c][d+1][0]!=0:           
            upright=p2 
    if a==2:#left
        if grill[c][d-1][0]==0 :
            reset=1
        if grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            right=1
        if grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            right=p1
        if grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            right=p1
        if grill[c+1][d][0]!=0 and grill[c-1][d][0]!=0:
            right= p
        if grill[c+1][d][0]!=0:
            downright=p2 
        if grill[c-1][d][0]!=0:          
            upright=p2 
        
    if a==3:#right
        if grill[c][d+1][0]==0 :
            reset=1
        if grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            left=1
        if grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            left=p1
        if grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            left=p1
        if grill[c+1][d][0]!=0 and grill[c-1][d][0]!=0:
            left= p
        if grill[c+1][d][0]!=0:
            downleft=p2 
        if grill[c-1][d][0]!=0:          
            upleft=p2 
            
    return up,down,left,right,reset,upleft,upright,downleft,downright

def calculR(grill, i,j,ax,p):
    c=i+1
    d=j+1
    p1=(1+p)/2
    p2=(1-p)/2
    if ax==0:#up
        if(grill[c-1][d][0]==0):

            a=-grill[c][d][0]
        elif grill[c-1][d-1][0]==0 and grill[c-1][d+1][0]==0:

            a= -grill[c-1][d][0]
        elif grill[c-1][d-1][0]==0 and grill[c-1][d+1][0]!=0:

            a=-grill[c-1][d][0]*p1-grill[c-1][d+1][0]*p2
        elif grill[c-1][d-1][0]!=0 and grill[c-1][d+1][0]==0:

            a=-grill[c-1][d][0]*p1-grill[c-1][d-1][0]*p2
        else: 

            a=-grill[c-1][d][0]*p-grill[c-1][d-1][0]*p2-grill[c-1][d+1][0]*p2
    if ax==1:#down
        if(grill[c+1][d][0]==0):

            a=-grill[c][d][0]
        elif grill[c+1][d-1][0]==0 and grill[c+1][d+1][0]==0:

            a= -grill[c+1][d][0]

        elif grill[c+1][d-1][0]==0 and grill[c+1][d+1][0]!=0:

            a=-grill[c+1][d][0]*p1-grill[c+1][d+1][0]*p2

        elif grill[c+1][d-1][0]!=0 and grill[c+1][d+1][0]==0:
            a=-grill[c+1][d][0]*p1-grill[c+1][d-1][0]*p2
        else: 
            a=-grill[c+1][d][0]*p-grill[c+1][d-1][0]*p2-grill[c+1][d+1][0]*p2
    if ax==2:#left
        if(grill[c][d-1][0]==0):
            
            a=-grill[c][d][0]
        elif grill[c+1][d-1][0]==0 and grill[c-1][d-1][0]==0:
            
            a= -grill[c][d-1][0]
        elif grill[c+1][d-1][0]==0 and grill[c-1][d-1][0]!=0:
            
            a=-grill[c][d-1][0]*p1-grill[c-1][d-1][0]*p2
        elif grill[c+1][d-1][0]!=0 and grill[c-1][d-1][0]==0:
            
            a=-grill[c][d-1][0]*p1-grill[c+1][d-1][0]*p2
        else:
            
            a=-grill[c][d-1][0]*p-grill[c+1][d-1][0]*p2-grill[c-1][d-1][0]*p2
        
    if ax==3:#right
        if(grill[c][d+1][0]==0):
            
            a=-grill[c][d][0]
        elif grill[c+1][d+1][0]==0 and grill[c-1][d+1][0]==0:
            
            a= -grill[c][d+1][0]
        elif grill[c+1][d+1][0]==0 and grill[c-1][d+1][0]!=0:
            
            a=-grill[c][d+1][0]*p1-grill[c-1][d+1][0]*p2
        elif grill[c+1][d+1][0]!=0 and grill[c-1][d+1][0]==0:
            
            a=-grill[c][d+1][0]*p1-grill[c+1][d+1][0]*p2
        else:
            
            a=-grill[c][d+1][0]*p-grill[c+1][d+1][0]*p2-grill[c-1][d+1][0]*p2
    return a


def optimale(n,m,nba,grill,p,gamma):
    
    # G : matrice des gains
   
    nbcont = n*m
    nbvar = n*m*nba
    count=0
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and  (i!=n-1 or j!=m-1)):
                count+=1

    # Range of plants and warehouses
    lignes = range(count)
    colonnes = range(nbvar)

    # Matrice des contraintes
    G=[]
    for i in range(n):
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                tab=np.zeros(n*m*nba)
                for a in range(nba):
                    tab[i*m*nba+j*nba+a]+=1
                    up,down,left,right,reset,upleft,upright,downleft,downright=calculTransfert(grill,i,j,a,p)
                    tab[i*m*nba+j*nba+a]-=reset*gamma
                    if(i>0):
                        tab[(i-1)*m*nba+j*nba+a]-=up*gamma
                    if(i<n-1):
                        tab[(i+1)*m*nba+j*nba+a]-=down*gamma
                    if(j>0):
                        tab[i*m*nba+(j-1)*nba+a]-=left*gamma
                    if(j<m-1):  
                        tab[i*m*nba+(j+1)*nba+a]-=right*gamma
                    if(i>0 and j>0):
                        tab[(i-1)*m*nba+(j-1)*nba+a]-=upleft*gamma
                    if(i>0 and j<m-1):
                        tab[(i-1)*m*nba+(j+1)*nba+a]-=upright*gamma
                    if(i<n-1 and j>0):
                        tab[(i+1)*m*nba+(j-1)*nba+a]-=downleft*gamma
                    if(i<n-1 and j<m-1):
                        tab[(i+1)*m*nba+(j+1)*nba+a]-=downright*gamma
                G.append(tab)
    G=np.array(G)
    # Second membre
   
    # Coefficients de la fonction objectif
    c = []
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                for a in range(nba):
                    r=calculR(grill, i,j,a,p)
                    c.append(r)
         
    m1 = Model("mogplex")     

    # declaration variables de decision
    x = []
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                for a in range(nba):
                    x.append(m1.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i*m*nba+j*nba+a+1)))

    # maj du modele pour integrer les nouvelles variables
    m1.update()

    obj = LinExpr();
    obj =0
    count=0
    for i in range(n) :
            for j in range(m):
                if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                    for a in range(nba):
                        obj += c[count] * x[count]
                        count+=1


    # definition de l'objectif
    m1.setObjective(obj,GRB.MAXIMIZE)
    m1.setParam("OutputFlag",False)
    # Definition des contraintes
    for nb in lignes:
        obj1 = LinExpr();
        obj1 =0
        count=0
        for i in range(n) :
            for j in range(m):
                if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                    for a in range(nba):
                        if(G[nb][i*m*nba+j*nba+a]!=0):
                            obj1+=G[nb][i*m*nba+j*nba+a]*x[count]
                        count+=1
               
        m1.addConstr(obj1 == 1)
    # Resolution
    m1.optimize()

    # print("")                
    # print('Solution optimale:')
    
    # print("")
    # print('Valeur de la fonction objectif :', m.objVal)
    # print("dico :",dico_opt)
    tab=np.zeros((n,m,nba))
    tab2=np.zeros((n,m))
    count=0
    for i in range(n):
        for j in range(m):
            tab1=[]
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                for a in range(nba):      
                    v=x[count].X
                    count+=1
                    tab1.append(v)
                amax=np.argmax(tab1)
                tab2[i][j]=amax
                if(grill[i+1][j+1][0]!=0):
                    v=tab1[amax]
                    if (v>0):
                        for el in tab1:
                            if el >0 and el!=v:
                                print(tab1) 
                        for e in range(nba):
                            tab[i][j][e]=tab1[e]/np.sum(tab1)

         
    return tab2

def optimalepure(n,m,nba,grill,p,gamma):
    
    # G : matrice des gains
   
    nbcont = n*m
    nbvar = n*m*nba
    count=0
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and  (i!=n-1 or j!=m-1)):
                count+=1

    # Range of plants and warehouses
    lignes = range(count)
    colonnes = range(nbvar)

    # Matrice des contraintes
    G=[]
    for i in range(n):
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                tab=np.zeros(n*m*nba)
                for a in range(nba):
                    tab[i*m*nba+j*nba+a]+=1
                    up,down,left,right,reset,upleft,upright,downleft,downright=calculTransfert(grill,i,j,a,p)
                    tab[i*m*nba+j*nba+a]-=reset*gamma
                    if(i>0):
                        tab[(i-1)*m*nba+j*nba+a]-=up*gamma
                    if(i<n-1):
                        tab[(i+1)*m*nba+j*nba+a]-=down*gamma
                    if(j>0):
                        tab[i*m*nba+(j-1)*nba+a]-=left*gamma
                    if(j<m-1):  
                        tab[i*m*nba+(j+1)*nba+a]-=right*gamma
                    if(i>0 and j>0):
                        tab[(i-1)*m*nba+(j-1)*nba+a]-=upleft*gamma
                    if(i>0 and j<m-1):
                        tab[(i-1)*m*nba+(j+1)*nba+a]-=upright*gamma
                    if(i<n-1 and j>0):
                        tab[(i+1)*m*nba+(j-1)*nba+a]-=downleft*gamma
                    if(i<n-1 and j<m-1):
                        tab[(i+1)*m*nba+(j+1)*nba+a]-=downright*gamma
                G.append(tab)
    G=np.array(G)
    # Second membre
   
    # Coefficients de la fonction objectif
    c = []
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                for a in range(nba):
                    r=calculR(grill, i,j,a,p)
                    c.append(r)
         
    m1 = Model("mogplex")     

    # declaration variables de decision
    x = []
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                for a in range(nba):
                    x.append(m1.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i*m*nba+j*nba+a+1)))
    d=[]
    tab=[]
    for i in range(n):
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)): 
                for a in range(nba): 
                    d.append(m1.addVar(vtype=GRB.BINARY, lb=0,ub=1))

    # maj du modele pour integrer les nouvelles variables
    m1.update()

    obj = LinExpr();
    obj =0
    count=0
    for i in range(n) :
            for j in range(m):
                if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                    for a in range(nba):
                        obj += c[count] * x[count]
                        count+=1

    # definition de l'objectif
    m1.setObjective(obj,GRB.MAXIMIZE)

    # Definition des contraintes
    for nb in lignes:
        obj1 = LinExpr();
        obj1 =0
        count=0
        for i in range(n) :
            for j in range(m):
                if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                    for a in range(nba):
                        if(G[nb][i*m*nba+j*nba+a]!=0):
                            obj1+=G[nb][i*m*nba+j*nba+a]*x[count]
                        count+=1
               
        m1.addConstr(obj1 == 1)
    count=0
    for i in range(n):
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                m1.addConstr(quicksum(d[count*nba+a] for a in range(nba)) <= 1, "Contraintess%d" % (i*m+j+nbcont))
                
                count+=1
    count=0
    for i in range(n):
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                for a in range(nba):
                    m1.addConstr((1-gamma)*x[count]<= d[count], "Contraintesssss%d" % (i+n*m+nbcont))
                    #print((1-gamma)*x[count]<= d[count])
                    count+=1
                    
    # for  i in colonnes:
    #     m1.addConstr(x[i]<= 1/(1-gamma), "Contraintesssss%d" % (i+n*m+nbcont))
    # Resolution
    m1.optimize()

    #print(d)
    # print("")                
    # print('Solution optimale:')
    
    # print("")
    # print('Valeur de la fonction objectif :', m.objVal)
    # print("dico :",dico_opt)
    tab=np.zeros((n,m,nba))
    tab2=np.zeros((n,m))
    count=0
    for i in range(n):
        for j in range(m):
            tab1=[]
            if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                for a in range(nba):      
                    v=x[count].X
                    count+=1
                    tab1.append(v)
                amax=np.argmax(tab1)
                tab2[i][j]=amax
                if(grill[i+1][j+1][0]!=0):
                    v=tab1[amax]
                    if (v>0):
                        for el in tab1:
                            if el >0 and el!=v:
                                print(tab1) 
                        for e in range(nba):
                            tab[i][j][e]=tab1[e]/np.sum(tab1)


    return tab2