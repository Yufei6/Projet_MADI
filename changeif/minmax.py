import gurobipy as gb
from gurobipy import *
import numpy as np
from recherche_policy import *
from pl_policy import *



def calculobj(i,j,ax,obj,tab,grill,p,n,m):

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
                            reward=calculobj(i,j,a,obj,grill1,grill,p,n,m)
                            rx.append(reward)
        r.append(rx)
    # Coefficients de la fonction objectif
     
    r=np.array(r)
    # declaration variables de decision

    z=m1.addVar(vtype=GRB.CONTINUOUS,lb=-50000)

    # maj du modele pour integrer les nouvelles variables


    obj = LinExpr();
    obj =z
    m1.setObjective(obj,GRB.MAXIMIZE)
    m1.setParam("OutputFlag",True)


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
    count1=0
    objtab=np.zeros(color)
    if(m1.status==GRB.OPTIMAL):
        for i in range(n):
            for j in range(m):
                tab1=[]
                if(grill[i+1][j+1][0]!=0 and (i!=n-1 or j!=m-1)):
                    for a in range(nba):      
                        v=x[count].X
                        count+=1
                        tab1.append(v)
                    sumtab=np.sum(tab1)
                    for a in range(nba):
                        tab[i][j][a]=tab1[a]/sumtab
                    for obj in range(color):
                        for a in range(nba):
                            objtab[obj]+=tab[i][j][a]*r[obj][count1+a]
                    count1+=nba
    else:
        tab=np.ones((n,m,nba))
        

    return tab ,objtab
def transfergrill(grill,n,m,color):
    newgrill=np.zeros((n+2,m+2,color))
    for i in range(n+2):
        for j in range(m+2):
            if(i!=n+1 and j!=m+1 ):
                for c in color:
                    if(grill[i][j][0]==c+1):
                        newgrill[i][j][c]=grill[i][j][1]
    return newgrill

def calculesperance(tab,grill1,n,m,color):
    oldgrill=change_grill(grill1)
    grill=transfergrill(oldgrill)
    m1 = Model("mogplex") 
    x = dict{}
    for i in range(n+2) :
        for j in range(m+2):
            for c in color:
                x[i][j][c]=m1.addVar(vtype=GRB.CONTINUOUS, lb=0)
    m1.update()
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(i!=n+1 and j!=m+1 ):
            for c in color:
                m1.addConstr(x[i][j][c] = tab[i-1][j-1][0]*(x[i-1][j-1][c]+grill[i-1][j-1][c]) \
                    +tab[i-1][j-1][1]*(x[i-1][j][c]+grill[i-1][j][c]) \
                    +tab[i-1][j-1][2]*(x[i-1][j+1][c]+grill[i-1][j+1][c]) \
                    +tab[i-1][j-1][3]*(x[i][j-1][c]+grill[i][j-1][c]) \
                    +tab[i-1][j-1][4]*(x[i][j][c]+grill[i][j][c]) \
                    +tab[i-1][j-1][5]*(x[i][j+1][c]+grill[i][j+1][c]) \
                    +tab[i-1][j-1][6]*(x[i+1][j-1][c]+grill[i+1][j-1][c]) \
                    +tab[i-1][j-1][7]*(x[i+1][j][c]+grill[i+1][j][c]) \
                    +tab[i-1][j-1][8]*(x[i+1][j+1][c]+grill[i+1][j+1][c]))

    for i in range(n+2) :
        for j in range(m+2):
            if(oldgrill[i][j][0]<=0)
                for c in color:
                    m1.addConstr(x[i][j][c]=0)


    obj = LinExpr();
    for c in color:
        obj +=x[1][1][c]
    m1.setObjective(obj,GRB.MINIMIZE)
    m1.setParam("OutputFlag",True)
    m1.optimize()
    print(obj)
    tab1=np.zeros(color)
    for c in color:
        tab1[c]=x[1][1][c].X
    return tab;