import numpy as np

def calculV(grill, n,m,i,j,a,p,tab,gamma):
    c=i+1
    d=j+1
    p1=(1+p)/2
    p2=(1-p)/2
    if a==0:#up
        if(grill[c-1][d][0]==0):
            a=tab[i][j]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            a= -grill[c-1][d][0]+gamma*tab[i-1][j]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            a=-grill[c-1][d][0]*p1-grill[c][d+1][0]*p2+gamma*(tab[i-1][j]*p1+tab[i][j+1]*p2)
        elif grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            a=-grill[c-1][d][0]*p1-grill[c][d-1][0]*p2+gamma*(tab[i-1][j]*p1+tab[i][j-1]*p2)
        else: 
            a=-grill[c-1][d][0]*p-grill[c][d-1][0]*p2+grill[c][d+1][0]*p2\
            +gamma*(tab[i-1][j]*p+tab[i][j-1]*p2+tab[i][j+1]*p2)
    if a==1:#down
        if(grill[c+1][d][0]==0):
            a=tab[i][j]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]==0:
            a= -grill[c+1][d][0]\
            +gamma*tab[i+1][j]
        elif grill[c][d-1][0]==0 and grill[c][d+1][0]!=0:
            a=-grill[c+1][d][0]*p1-grill[c][d+1][0]*p2\
            +gamma*(tab[i+1][j]*p1+tab[i][j+1]*p2)
        elif grill[c][d-1][0]!=0 and grill[c][d+1][0]==0:
            a=-grill[c+1][d][0]*p1-grill[c][d-1][0]*p2\
            +gamma*(tab[i+1][j]*p1+tab[i][j-1]*p2)
        else: 
            a=-grill[c+1][d][0]*p-grill[c][d-1][0]*p2+grill[c][d+1][0]*p2\
            +gamma*(tab[i+1][j]*p+tab[i][j-1]*p2+tab[i][j+1]*p2)
    if a==2:#left
        if(grill[c][d-1][0]==0):
            
            a=tab[i][j]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            
            a= -grill[c][d-1][0]\
            +gamma*tab[i][j-1]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            
            a=-grill[c][d-1][0]*p1-grill[c-1][d][0]*p2\
            +gamma*(tab[i][j-1]*p1+tab[i-1][j]*p2)
        elif grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            
            a=-grill[c][d-1][0]*p1-grill[c+1][d][0]*p2\
            +gamma*(tab[i][j-1]*p1+tab[i+1][j]*p2)
        else:
            
            a=-grill[c][d-1][0]*p-grill[c+1][d][0]*p2+grill[c-1][d][0]*p2\
            +gamma*(tab[i][j-1]*p+tab[i+1][j]*p2+tab[i-1][j]*p2)
        
    if a==3:#right
        if(grill[c][d+1][0]==0):
            
            a=tab[i][j]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]==0:
            
            a= -grill[c][d+1][0]\
            +gamma*tab[i][j+1]
        elif grill[c+1][d][0]==0 and grill[c-1][d][0]!=0:
            
            a=-grill[c][d+1][0]*p1-grill[c-1][d][0]*p2\
            +gamma*(tab[i][j+1]*p1+tab[i-1][j]*p2)
        elif grill[c+1][d][0]!=0 and grill[c-1][d][0]==0:
            
            a=-grill[c][d+1][0]*p1-grill[c+1][d][0]*p2\
            +gamma*(tab[i][j+1]*p1+tab[i+1][j]*p2)
        else:
            
            a=-grill[c][d+1][0]*p-grill[c+1][d][0]*p2+grill[c-1][d][0]*p2\
            +gamma*(tab[i][j+1]*p+tab[i+1][j]*p2+tab[i-1][j]*p2)
        
def itervalue(grill, n,m,p,gamma,e):
    tabaction=np.zeros(n,m)
    tab=np.zeros(n,m)
    tab_ancien= np.zeros(n,m)
    for t in range(10000):
        tab_ancien=tab
        for i in range(n):
            for j in range(m):
                temp=np.zeros(3)
                for a in range(3):
                    temp[a]=calculV(grill,n,m,i,j,a,p,tab_ancien,gamma)
                tab[i][j]=max(temp)
                tabaction[i][j]=np.argmax(temp)
        diffmax=0
        for i in range(n):
            for j in range(m):
                diff=tab[i][j]-tab_ancien[i][j]
                if diff>diffmax:
                    diffmax=diff
        if diffmax<e:
            break
    return tabaction