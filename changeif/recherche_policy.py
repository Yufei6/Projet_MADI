import numpy as np
import math

def transfer_puissance(grill,_q):
    for i in range(len(grill)):
        for j in range(len(grill[0])):
            if grill[i,j,0]!=5 and grill[i,j,0]>0:
                grill[i,j,0] = grill[i,j,0] ** _q
    return grill

def transfer_objectif(grill, objectif):
    for i in range(len(grill)):
        for j in range(len(grill[0])):
            if grill[i,j,0]==5:
                grill[i,j,0] = -1 * objectif
    return grill

def transfer_color(grill, objectif):
    for i in range(len(grill)):
        for j in range(len(grill[0])):
            if grill[i,j,0]==4:
                grill[i,j,0] = grill[i,j,0] * 10000**3
            elif grill[i,j,0]==3:
                grill[i,j,0] = grill[i,j,0] * 10000**2
            elif grill[i,j,0]==2:
                grill[i,j,0] = grill[i,j,0] * 10000
            elif grill[i,j,0]==-1 * objectif:
                grill[i,j,0] = grill[i,j,0] * 10000**3
                print("change",grill[i,j,0])
    return grill

def calculV(grill, n,m,i,j,a,p,tab,gamma):
    c=i+1
    d=j+1
    p1=(1+p)/2
    p2=(1-p)/2
    if a==0:#up
        if(grill[c-1][d][0]==0):
            b=tab[i][j]-grill[c][d][0]
        elif grill[c-1][d-1][0]==0 and grill[c-1][d+1][0]==0:
            b= -grill[c-1][d][0]+gamma*tab[i-1][j]

        elif grill[c-1][d-1][0]==0 and grill[c-1][d+1][0]!=0:
            b=-grill[c-1][d][0]*p1-grill[c-1][d+1][0]*p2+gamma*(tab[i-1][j]*p1+tab[i-1][j+1]*p2)

        elif grill[c-1][d-1][0]!=0 and grill[c-1][d+1][0]==0:

            b=-grill[c-1][d][0]*p1-grill[c-1][d-1][0]*p2+gamma*(tab[i-1][j]*p1+tab[i-1][j-1]*p2)

        else: 

            b=-grill[c-1][d][0]*p-grill[c-1][d-1][0]*p2+grill[c-1][d+1][0]*p2\
            +gamma*(tab[i-1][j]*p+tab[i-1][j-1]*p2+tab[i-1][j+1]*p2)
    if a==1:#down
        if(grill[c+1][d][0]==0):

            b=tab[i][j]-grill[c][d][0]
        elif grill[c+1][d-1][0]==0 and grill[c+1][d+1][0]==0:

            b= -grill[c+1][d][0]\
            +gamma*tab[i+1][j]
        elif grill[c+1][d-1][0]==0 and grill[c+1][d+1][0]!=0:

            b=-grill[c+1][d][0]*p1-grill[c+1][d+1][0]*p2\
            +gamma*(tab[i+1][j]*p1+tab[i+1][j+1]*p2)
        elif grill[c+1][d-1][0]!=0 and grill[c+1][d+1][0]==0:

            b=-grill[c+1][d][0]*p1-grill[c+1][d-1][0]*p2\
            +gamma*(tab[i+1][j]*p1+tab[i+1][j-1]*p2)
        else: 

            b=-grill[c+1][d][0]*p-grill[c+1][d-1][0]*p2+grill[c+1][d+1][0]*p2\
            +gamma*(tab[i+1][j]*p+tab[i+1][j-1]*p2+tab[i+1][j+1]*p2)
    if a==2:#left
        if(grill[c][d-1][0]==0):
            
            b=tab[i][j]-grill[c][d][0]
        elif grill[c+1][d-1][0]==0 and grill[c-1][d-1][0]==0:
            
            b= -grill[c][d-1][0]\
            +gamma*tab[i][j-1]
        elif grill[c+1][d-1][0]==0 and grill[c-1][d-1][0]!=0:
            
            b=-grill[c][d-1][0]*p1-grill[c-1][d-1][0]*p2\
            +gamma*(tab[i][j-1]*p1+tab[i-1][j-1]*p2)
        elif grill[c+1][d-1][0]!=0 and grill[c-1][d-1][0]==0:
            
            b=-grill[c][d-1][0]*p1-grill[c+1][d-1][0]*p2\
            +gamma*(tab[i][j-1]*p1+tab[i+1][j-1]*p2)
        else:
            
            b=-grill[c][d-1][0]*p-grill[c+1][d-1][0]*p2+grill[c-1][d-1][0]*p2\
            +gamma*(tab[i][j-1]*p+tab[i+1][j-1]*p2+tab[i-1][j-1]*p2)
        
    if a==3:#right
        if(grill[c][d+1][0]==0):
            
            b=tab[i][j]-grill[c][d][0]
        elif grill[c+1][d+1][0]==0 and grill[c-1][d+1][0]==0:
            
            b= -grill[c][d+1][0]\
            +gamma*tab[i][j+1]
        elif grill[c+1][d+1][0]==0 and grill[c-1][d+1][0]!=0:
            
            b=-grill[c][d+1][0]*p1-grill[c-1][d+1][0]*p2\
            +gamma*(tab[i][j+1]*p1+tab[i-1][j+1]*p2)
        elif grill[c+1][d+1][0]!=0 and grill[c-1][d+1][0]==0:
            
            b=-grill[c][d+1][0]*p1-grill[c+1][d+1][0]*p2\
            +gamma*(tab[i][j+1]*p1+tab[i+1][j+1]*p2)
        else:
            
            b=-grill[c][d+1][0]*p-grill[c+1][d+1][0]*p2+grill[c-1][d+1][0]*p2\
            +gamma*(tab[i][j+1]*p+tab[i+1][j+1]*p2+tab[i-1][j+1]*p2)
            
    return b

def change_grill(grill,n,m, objectif):
    grill = transfer_objectif(grill, objectif)
    new_grill = np.zeros((n+2, m+2, 2))
    for i in range(n+2):
        for j in range(m+2):
            if i==0 or i==n+1 or j==0 or j==m+1:
                new_grill[i,j,0] = 0
                new_grill[i,j,1] = 0
            else:
                new_grill[i,j,0] = grill[i-1,j-1,0]
                new_grill[i,j,1] = grill[i-1,j-1,1]
    return new_grill

#Baowei return False
def check_grill(i,j,grill):
    c=i+1
    d=j+1
    if (grill[c-1][d][0]==0) and (grill[c+1][d][0]==0) and (grill[c][d-1][0]==0) and (grill[c][d+1][0]==0):
        return False
    return True
        
def itervalue(grill, n,m,p,gamma,e, objectif,_q=1, _color=False):
    #print("grill",grill)
    grill = transfer_puissance(grill,_q)
    grill = change_grill(grill, n, m, objectif)
    if _color:
        grill = transfer_color(grill,objectif)
    tabaction=np.zeros((n,m))
    tab=np.zeros((n,m))
    tab_ancien= np.zeros((n,m))
    iteration = 0
    while True:
        iteration +=1
        tab_ancien= np.copy(tab)
        for i in range(n):
            for j in range(m):
                if not (i==n-1 and j ==m-1):
                    if check_grill(i,j,grill):
                        temp=np.zeros(4)
                        for a in range(4):
                            temp[a]=calculV(grill,n,m,i,j,a,p,tab_ancien,gamma)
                        tab[i][j]=max(temp)
                        tabaction[i][j]=np.argmax(temp)
        #print("tab",tab)
        diffmax=0
        for i in range(n):
            for j in range(m):
                diff=abs(tab[i][j]-tab_ancien[i][j])
                if diff > diffmax:
                    diffmax = diff
        #print("diffmax", diffmax, " iteration",iteration)
        if diffmax <= e:
            #print("tabaction",tabaction)
            #print("tab",tab)
            return tabaction, iteration
