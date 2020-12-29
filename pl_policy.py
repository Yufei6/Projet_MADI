import gurobipy as gb
from gurobipy import *
import numpy as np

def calculTransfert(grill,i,j,a,p):
    
    c=i+1
    d=j+1
    p1=(1+p)/2
    p2=(1-p)/2
    if a==0:#up
        if(grill[c-1][d][0]==0):
            up,down,left,right,reset=0,0,0,0,1
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            up,down,left,right,reset=1,0,0,0,0
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            up,down,left,right,reset=p1,0,0,p2,0
        elif grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            up,down,left,right,reset=p1,0,p2,0,0
        else: 
            up,down,left,right,reset=p,0,p2,p2,0
    if a==1:#down
        if(grill[c+1][d][0]==0):
            up,down,left,right,reset=0,0,0,0,1
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            up,down,left,right,reset=0,1,0,0,0
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            up,down,left,right,reset=0,p1,0,p2,0
        elif grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            up,down,left,right,reset=0,p1,p2,0,0
        else: 
           up,down,left,right,reset=0,p,p2,p2,0
    if a==2:#left
        if(grill[c][d-1][0]==0):
            up,down,left,right,reset=0,0,0,0,1
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            
            up,down,left,right,reset=0,0,1,0,0
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            
            up,down,left,right,reset=p2,0,p1,0,0
        elif grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            
            up,down,left,right,reset=0,p2,p1,0,0
        else:
            
            up,down,left,right,reset=p2,p2,p,0,0
        
    if a==3:#right
        if(grill[c][d+1][0]==0):
            
            up,down,left,right,reset=0,0,0,0,1
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            
            up,down,left,right,reset=0,0,0,1,0
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            
            up,down,left,right,reset=p2,0,0,p1,0
        elif grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            
            up,down,left,right,reset=0,p2,0,p1,0
        else:
            up,down,left,right,reset=p2,p2,0,p,0
            
    return up,down,left,right,reset

def calculR(grill, i,j,ax,p):
    c=i+1
    d=j+1
    p1=(1+p)/2
    p2=(1-p)/2
    if ax==0:#up
        if(grill[c-1][d][0]==0):
            a=-grill[i][j][0]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            a= -grill[c-1][d][0]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            a=-grill[c-1][d][0]*p1-grill[c][d+1][0]*p2
        elif grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            a=-grill[c-1][d][0]*p1-grill[c][d-1][0]*p2
        else: 
            a=-grill[c-1][d][0]*p-grill[c][d-1][0]*p2+grill[c][d+1][0]*p2
    if ax==1:#down
        if(grill[c+1][d][0]==0):
            a=-grill[i][j][0]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            a= -grill[c+1][d][0]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            a=-grill[c+1][d][0]*p1-grill[c][d+1][0]*p2
        elif grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            a=-grill[c+1][d][0]*p1-grill[c][d-1][0]*p2
        else: 
            a=-grill[c+1][d][0]*p-grill[c][d-1][0]*p2+grill[c][d+1][0]*p2
    if ax==2:#left
        if(grill[c][d-1][0]==0):
            
            a=-grill[i][j][0]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            
            a= -grill[c][d-1][0]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            
            a=-grill[c][d-1][0]*p1-grill[c-1][d][0]*p2
        elif grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            
            a=-grill[c][d-1][0]*p1-grill[c+1][d][0]*p2
        else:
            
            a=-grill[c][d-1][0]*p-grill[c+1][d][0]*p2+grill[c-1][d][0]*p2
        
    if ax==3:#right
        if(grill[c][d+1][0]==0):
            
            a=-grill[i][j][0]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            
            a= -grill[c][d+1][0]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            
            a=-grill[c][d+1][0]*p1-grill[c-1][d][0]*p2
        elif grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            
            a=-grill[c][d+1][0]*p1-grill[c+1][d][0]*p2
        else:
            
            a=-grill[c][d+1][0]*p-grill[c+1][d][0]*p2+grill[c-1][d][0]*p2
    return a


def optimale(n,m,nba,grill,p,gamma):
    
    # G : matrice des gains
   

    nbcont = n*m
    nbvar = n*m*nba

    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)

    # Matrice des contraintes
    G=[]
    for i in range(n):
        for j in range(m):
            tab=np.zeros(n*m*nba)
            for a in range(nba):
                tab[i*m*nba+j*nba+a]+=1
                if(grill[i+1][j+1][0]!=0):
                    up,down,left,right,reset=calculTransfert(grill,i,j,a,p)
                    tab[i*m*nba+j*nba+a]+=reset*gamma
                    if(i>0):
                        tab[(i-1)*m*nba+j*nba+a]+=up*gamma
                    if(i<n-1):
                        tab[(i+1)*m*nba+j*nba+a]+=down*gamma
                    if(j>0):
                        tab[i*m*nba+(j-1)*nba+a]+=left*gamma
                    if(j<n-1):  
                        tab[i*m*nba+(j-1)*nba+a]+=right*gamma
            G.append(tab)
    G=np.array(G)
    # Second membre
    b = []
    
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]==0):
                b.append(0)
            else:
                b.append(1)
    # Coefficients de la fonction objectif
    c = []
    for i in range(n) :
        for j in range(m):
            for a in range(nba):
                r=calculR(grill, i,j,a,p)
                c.append(r)

         
    m1 = Model("mogplex")     

    # declaration variables de decision
    x = []
    for i in colonnes:
        x.append(m1.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i+1)))

    # maj du modele pour integrer les nouvelles variables
    m1.update()

    obj = LinExpr();
    obj =0
    for j in colonnes:
        obj += c[j] * x[j]

    # definition de l'objectif
    m1.setObjective(obj,GRB.MAXIMIZE)
    m1.setParam("OutputFlag",False)
    # Definition des contraintes
    for i in lignes:
        m1.addConstr(quicksum(G[i][j]*x[j] for j in colonnes) == b[i], "Contrainte%d" % i)

    # Resolution
    m1.optimize()


    # print("")                
    # print('Solution optimale:')
    
    # print("")
    # print('Valeur de la fonction objectif :', m.objVal)
    # print("dico :",dico_opt)
    tab=[]
    for i in range(n):
        for j in range(m):
            tab1=[]
            for a in range(nba):
                
                v=x[i*m*nba+j*nba+a].X
                tab1.append(v)
            amax=np.argmax(tab1)
            v=tab1[amax]
            if (v>0):
                for el in tab1:
                    if el >0 and el!=v:
                        print(tab1)   
            tab.append(tab1)
    
    return tab

def optimalepure(n,m,nba,grill,p,gamma):
    
    # G : matrice des gains
   

    nbcont = n*m
    nbvar = n*m*nba

    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)

    # Matrice des contraintes
    G=[]
    for i in range(n):
        for j in range(m):
            tab=np.zeros(n*m*nba)
            for a in range(nba):
                tab[i*m*nba+j*nba+a]+=1
                if(grill[i+1][j+1][0]!=0):
                    up,down,left,right,reset=calculTransfert(grill,i,j,a,p)
                    tab[i*m*nba+j*nba+a]+=reset*gamma
                    if(i>0):
                        tab[(i-1)*m*nba+j*nba+a]+=up*gamma
                    if(i<n-1):
                        tab[(i+1)*m*nba+j*nba+a]+=down*gamma
                    if(j>0):
                        tab[i*m*nba+(j-1)*nba+a]+=left*gamma
                    if(j<n-1):  
                        tab[i*m*nba+(j-1)*nba+a]+=right*gamma
            G.append(tab)
    G=np.array(G)
    # Second membre
    b = []
    
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]==0):
                b.append(0)
            else:
                b.append(1)
    # Coefficients de la fonction objectif
    c = []
    for i in range(n) :
        for j in range(m):
            for a in range(nba):
                print(a)
                r=calculR(grill, i,j,a,p)
                c.append(r)

         
    m1 = Model("mogplex")     

    # declaration variables de decision
    x = []
    for i in colonnes:
        x.append(m1.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i+1)))
    d=[]
    tab=[]
    for i in range(n):
        for j in range(m): 
            for a in range(nba): 
                d.append(m1.addVar(vtype=GRB.BINARY, lb=0,ub=1))

    # maj du modele pour integrer les nouvelles variables
    m1.update()

    obj = LinExpr();
    obj =0
    for j in colonnes:
        obj += c[j] * x[j]

    # definition de l'objectif
    m1.setObjective(obj,GRB.MAXIMIZE)

    # Definition des contraintes
    for i in lignes:
        m1.addConstr(quicksum(G[i][j]*x[j] for j in colonnes) == b[i], "Contrainte%d" % i)
    for i in range(n):
        for j in range(m):
            m1.addConstr(quicksum(d[i*m*nba+j*nba+a] for a in range(nba)) <= 1, "Contrainte%d" % (i*m+j+nbcont))
    for i in colonnes:
        m1.addConstr((1-gamma)*x[i]<= d[i], "Contrainte%d" % (i+n*m+nbcont))

    # Resolution
    m1.optimize()


    # print("")                
    # print('Solution optimale:')
    
    # print("")
    # print('Valeur de la fonction objectif :', m.objVal)
    # print("dico :",dico_opt)
    tab=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            tab1=[]
            for a in range(nba):
                
                v=x[i*m*nba+j*nba+a].X
                tab1.append(v)
            amax=np.argmax(tab1)
            v=tab1[amax]
            if (v>0):
                for el in tab1:
                    if el >0 and el!=v:
                        print("error")   
            tab[i][j]=amax

    return tab