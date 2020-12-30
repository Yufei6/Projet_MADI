import gurobipy as gb
from gurobipy import *
import numpy as np
from recherche_policy import *
from pl_policy import *



def calculobj(i,j,ax,obj,tab,grill,p):

    c=i+1
    d=j+1
    p1=(1+p)/2
    p2=(1-p)/2
    if ax==0:#up
        if(grill[c-1][d][0]==0 ):

            a=-tab[i][j][1]*(grill[c][d][0]==obj)
        elif grill[c-1][d-1][0]==0 and grill[c-1][d+1][0]==0 :

            a= -tab[i-1][j][1]*(grill[c-1][d][0]==obj)
        elif grill[c-1][d-1][0]==0 and grill[c-1][d+1][0]!=0:

            a=-tab[i-1][j][1]*p1*(grill[c-1][d][0]==obj)\
            -tab[i-1][j+1][1]*p2*(grill[c-1][d+1][0]==obj)
        elif grill[c-1][d-1][0]!=0 and grill[c-1][d+1][0]==0:

            a=-tab[i-1][j][1]*p1*(grill[c-1][d][0]==obj)\
            -tab[i-1][j-1][1]*p2*(grill[c-1][d-1][0]==obj)
        else: 

            a=-tab[i-1][j][1]*p*(grill[c-1][d][0]==obj)\
            -tab[i-1][j-1][1]*p2*(grill[c-1][d-1][0]==obj)-tab[i-1][j+1][1]*p2*(grill[c-1][d+1][0]==obj)
    if ax==1:#down
        if(grill[c+1][d][0]==0 ):

            a=-tab[i][j][1]*(grill[c][d][0]==obj)
        elif grill[c+1][d-1][0]==0 and grill[c+1][d+1][0]==0 :

            a= -tab[i+1][j][1]*(grill[c+1][d][0]==obj)
        elif grill[c+1][d-1][0]==0 and grill[c+1][d+1][0]!=0:

            a=-tab[i+1][j][1]*p1*(grill[c+1][d][0]==obj)\
            -tab[i+1][j+1][1]*p2*(grill[c+1][d+1][0]==obj)
        elif grill[c+1][d-1][0]!=0 and grill[c+1][d+1][0]==0:

            a=-tab[i+1][j][1]*p1*(grill[c+1][d][0]==obj)\
            -tab[i+1][j-1][1]*p2*(grill[c+1][d-1][0]==obj)
        else: 

            a=-tab[i+1][j][1]*p*(grill[c+1][d][0]==obj)\
            -tab[i+1][j-1][1]*p2*(grill[c+1][d-1][0]==obj)-tab[i+1][j+1][1]*p2*(grill[c+1][d+1][0]==obj)
    if ax==2:#left
        if(grill[c][d-1][0]==0 ):

            a=-tab[i][j][1]*(grill[c][d][0]==obj)
        elif grill[c+1][d-1][0]==0 and grill[c-1][d-1][0]==0 :

            a= -tab[i][j-1][1]*(grill[c][d-1][0]==obj)
        elif grill[c+1][d-1][0]==0 and grill[c-1][d-1][0]!=0:

            a=-tab[i][j-1][1]*p1*(grill[c][d-1][0]==obj)\
            -tab[i-1][j-1][1]*p2*(grill[c-1][d-1][0]==obj)
        elif grill[c+1][d-1][0]!=0 and grill[c-1][d-1][0]==0:

            a=-tab[i][j-1][1]*p1*(grill[c][d-1][0]==obj)\
            -tab[i+1][j-1][1]*p2*(grill[c+1][d-1][0]==obj)
        else: 

            a=-tab[i][j-1][1]*p*(grill[c][d-1][0]==obj)\
            -tab[i-1][j-1][1]*p2*(grill[c-1][d-1][0]==obj)-tab[i+1][j-1][1]*p2*(grill[c+1][d-1][0]==obj)
        
    if ax==3:#right
        if(grill[c][d+1][0]==0 ):

            a=-tab[i][j][1]*(grill[c][d][0]==obj)
        elif grill[c+1][d+1][0]==0 and grill[c-1][d+1][0]==0 :

            a= -tab[i][j+1][1]*(grill[c][d+1][0]==obj)
        elif grill[c+1][d+1][0]==0 and grill[c-1][d+1][0]!=0:

            a=-tab[i][j+1][1]*p1*(grill[c][d+1][0]==obj)\
            -tab[i-1][j+1][1]*p2*(grill[c-1][d+1][0]==obj)
        elif grill[c+1][d+1][0]!=0 and grill[c-1][d+1][0]==0:

            a=-tab[i][j+1][1]*p1*(grill[c][d+1][0]==obj)\
            -tab[i+1][j+1][1]*p2*(grill[c+1][d+1][0]==obj)
        else: 
            a=-tab[i][j+1][1]*p*(grill[c][d+1][0]==obj)\
            -tab[i-1][j+1][1]*p2*(grill[c-1][d+1][0]==obj)-tab[i+1][j+1][1]*p2*(grill[c+1][d+1][0]==obj)
    return a


def multioptimale(n,m,nba,grill1,p,gamma,objectif,color):
    
    # G : matrice des gains

    grill=change_grill(grill1,n,m,objectif)
    print(grill1[n-1][m-1][1])
    
    nbcont = n*m
    nbvar = n*m*nba
    count=0
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and  (i!=n-1 or j!=m-1)):
                count+=1

    # Range of plants and warehouses
    lignes = range(count)
    count=0
    for i in range(n) :
        for j in range(m):
            if(grill[i+1][j+1][0]!=0 and  (i!=n-1 or j!=m-1)):
                for a in range(nba):
                    count+=1

    colonnes = range(count)

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




    # definition de l'objectif
    
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
    # Second membre


    r = []
    for obj in range(1,color+1):
        rx=[]
        for i in range(n):
            for j in range(m):
                if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                    for a in range(nba):
                            reward=calculobj(i,j,a,obj,grill1,grill,p)
                            rx.append(reward)
        r.append(rx)
    # Coefficients de la fonction objectif
     
    r=np.array(r)
    # declaration variables de decision

    z=m1.addVar(vtype=GRB.CONTINUOUS,lb=-500)

    # maj du modele pour integrer les nouvelles variables


    obj = LinExpr();
    obj =z
    m1.setObjective(obj,GRB.MAXIMIZE)
    m1.setParam("OutputFlag",False)


    # definition de l'objectif

    for obj in range(color):
        m1.addConstr(z <= quicksum(r[obj][j]*x[j] for j in colonnes))
        
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
    print(z.x)

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
