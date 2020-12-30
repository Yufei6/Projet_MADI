import gurobipy as gb
from gurobipy import *
import numpy as np

def pdm4():




















def multioptimale(n,m,nba,grill,p,gamma):
    
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

    r = []
    for obj in range(objectif):
	    for i in range(n):
	    	for j in range(m):
	    		for a in range(nba):
	    			
	    				reward=calculobj(i,j,a,obj)
	    				r.append(reward)
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
    z=m1.addVar(vtype=GRB.CONTINUOUS, lb=0)

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
    for obj in range(objectif):
    	m1.addConstr(z <= quicksum(r[obj][j]*x[j] for j in colonnes), "Contraintes%d" % obj)
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
            if(grill[i+1][j+1][0]!=0):
            v=tab1[amax]
            if (v>0):
                for el in tab1:
                    if el >0 and el!=v:
                        print(tab1)   
            tab.append(tab1)
    
    return tab