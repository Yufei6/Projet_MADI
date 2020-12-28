from tkinter import *
import numpy as np

def check_up(cj,li):
	if li>0:
		if g[li-1,cj][0]>0:
			return True
	return False

def check_down(cj,li):
	if li<nblignes-1:
		if g[li+1,cj][0]>0:
			return True
	return False

def check_right(cj,li):
	if cj<nbcolonnes-1:
		if g[li,cj+1][0]>0:
			return True
	return False

def check_left(cj,li):
	if cj>0:
		if g[li,cj-1][0]>0:
			return True
	return False

def move_proba_up(cj, li):
	global PosX,PosY,cost,g
	cu = check_left(cj,li)
	cd = check_down(cj,li)
	cl = check_left(cj,li)
	cr = check_right(cj,li)
	if not cl and not cr:
		PosY -= zoom*20
		cost[g[li-1,cj,0]]+=g[li-1,cj,1]
	else:
		p=np.random.uniform(0,1)
		if cl and cr:
			p0 = proba
			p1 = (1-proba)/2
			if p < p0:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
			elif p < p0+p1:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 
			else:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
		elif cl and not cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
			else:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
		elif not cl and cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
			else:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 

def move_proba_down(cj, li):
	global PosX,PosY,cost,g
	cu = check_left(cj,li)
	cd = check_down(cj,li)
	cl = check_left(cj,li)
	cr = check_right(cj,li)
	if not cl and not cr:
		PosY += zoom*20
	else:
		p=np.random.uniform(0,1)
		if cl and cr:
			p0 = proba
			p1 = (1-proba)/2
			if p < p0:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 
			elif p < p0+p1:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 
			else:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
		elif cl and not cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 
			else:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
		elif not cl and cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 
			else:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 

def move_proba_right(cj, li):
	global PosX,PosY,cost,g
	cu = check_left(cj,li)
	cd = check_down(cj,li)
	cl = check_left(cj,li)
	cr = check_right(cj,li)
	if not cu and not cd:
		PosX += zoom*20
	else:
		p=np.random.uniform(0,1)
		if cu and cd:
			p0 = proba
			p1 = (1-proba)/2
			if p < p0:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 
			elif p < p0+p1:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 
			else:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
		elif cu and not cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 
			else:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
		elif not cu and cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 
			else:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 

def move_proba_left(cj, li):
	global PosX,PosY,cost,g
	cu = check_left(cj,li)
	cd = check_down(cj,li)
	cl = check_left(cj,li)
	cr = check_right(cj,li)
	if not cu and not cd:
		PosX -= zoom*20
	else:
		p=np.random.uniform(0,1)
		if cu and cd:
			p0 = proba
			p1 = (1-proba)/2
			if p < p0:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
			elif p < p0+p1:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 
			else:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
		elif cu and not cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
			else:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
		elif not cu and cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
			else:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 

def initialize():
	global PosX,PosY,cost
# position initiale du robot
	PosX = 20+10*zoom
	PosY = 20+10*zoom
	for k in range(5):
		cost[k]=0
# cout et affichage
	Canevas.coords(Pion,PosX -9*zoom, PosY -9*zoom, PosX +9*zoom, PosY +9*zoom)
	wg.config(text=str(cost[1]))
	wb.config(text=str(cost[2]))
	wr.config(text=str(cost[3]))
	wn.config(text=str(cost[4]))
	ws.config(text='     total = '+str(cost[0]))
	


def Clavier(event):
	global PosX,PosY
	touche = event.keysym
	cj=round((PosX-30)/(20*zoom))
	li=round((PosY-30)/(20*zoom))
	# print(li,cj)
	# deplacement vers le haut
	if touche == 'Up' and check_up(cj,li):
		move_proba_up(cj, li)
	# deplacement vers le bas
	if touche == 'Down' and check_down(cj,li):
		move_proba_down(cj, li)
	# deplacement vers la droite
	if touche == 'Right' and check_right(cj,li):
		move_proba_right(cj, li)
	# deplacement vers la gauche
	if touche == 'Left' and check_left(cj,li):
		move_proba_left(cj, li)
	# on dessine le pion a sa nouvelle position
	Canevas.coords(Pion,PosX -9*zoom, PosY -9*zoom, PosX +9*zoom, PosY +9*zoom)
	cost[0]=0    
	for k in range(4):
		cost[0]+=cost[k+1]*weight[k+1]        
	wg.config(text=str(cost[1]))
	wb.config(text=str(cost[2]))
	wr.config(text=str(cost[3]))
	wn.config(text=str(cost[4]))
	ws.config(text='     total = '+str(cost[0]))


def colordraw(g,nblignes,nbcolonnes):
	pblanc=0.1
	pverte=0.3
	pbleue=0.25
	prouge=0.2
	pnoire=0.15
	for i in range(nblignes):
		for j in range(nbcolonnes):
			y =20*i+20
			x =20*j+20
			z=np.random.uniform(0,1)
			if z < pblanc:
				c=0
			else:
				if z < pblanc+ pverte:
					c=1
				else:
					if z < pblanc+ pverte + pbleue:
						c=2
					else:
						if z< pblanc+ pverte + pbleue +prouge:
							c=3
						else:
							c=4            
			if c>0:
				g[i,j,0]=c
				g[i,j,1]=np.random.randint(1, 9 + 1)
	g[0,0,0]=np.random.randint(1, 3 + 1)
	g[0,1,0]=np.random.randint(1, 3 + 1)
	g[2,0,0]=np.random.randint(1, 3 + 1)
	g[nblignes-1,nbcolonnes-1]=np.random.randint(1, 3 + 1)
	g[nblignes-2,nbcolonnes-1]=np.random.randint(1, 3 + 1)
	g[nblignes-1,nbcolonnes-2]=np.random.randint(1, 3 + 1)
	for i in range(nblignes):
		for j in range(nbcolonnes):          
			y =zoom*20*i+20
			x =zoom*20*j+20
			if g[i,j,0]>0:            
				#Canevas.create_oval(x+zoom*(10-3),y+zoom*(10-3),x+zoom*(10+3),y+zoom*(10+3),width=1,outline=color[g[i,j]],fill=color[g[i,j]])
				Canevas.create_text(x+zoom*(10),y+zoom*(10), text=str(g[i,j,1]),fill=color[g[i,j,0]],font = "Verdana "+str(int(6*zoom))+" bold")
			else:
				Canevas.create_rectangle(x, y, x+zoom*20, y+zoom*20, fill=mywalls)
	print("GGG",g)




if __name__ == "__main__":
	#taille de la grille
	nblignes=20
	nbcolonnes=15
	proba = 0.8
	zoom=2


	Mafenetre = Tk()
	Mafenetre.title('MADI PROJET')

	# position initiale du pion
	PosX = 20+10*zoom
	PosY = 20+10*zoom

	# Creation d'un widget Canvas (zone graphique)
	Largeur = zoom*20*nbcolonnes+40
	Hauteur = zoom*20*nblignes+40
	 
	# valeurs de la grille
	g = np.zeros((nblignes,nbcolonnes,2), dtype=np.int)
	cost= np.zeros(5, dtype=np.int)
	weight= np.zeros(5, dtype=np.int)
	weight[1] = 1
	weight[2] = 1
	weight[3] = 1
	weight[4] = 1

	myred="#F70B42"
	mygreen="#1AD22C"
	myblue="#0B79F7"
	mygrey="#E8E8EB"
	myyellow="#F9FB70"
	myblack="#5E5E64"
	mywalls="#5E5E64"
	mywhite="#FFFFFF"

	color=[mywhite,mygreen,myblue,myred,myblack]

	Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg =mywhite)
	for i in range(nblignes+2):
		ni=zoom*20*i+20
		Canevas.create_line(20, ni, Largeur-20,ni)
	for j in range(nbcolonnes+2):
		nj=zoom*20*j+20
		Canevas.create_line(nj, 20, nj, Hauteur-20)
	colordraw(g,nblignes,nbcolonnes)
	Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,outline='black',fill=myyellow)
	Canevas.focus_set()
	Canevas.bind('<Key>',Clavier)
	Canevas.pack(padx =5, pady =5)

	# Craation d'un widget Button (bouton Quitter)
	# Creation d'un widget Button (bouton Quitter)
	Button(Mafenetre, text ='Restart', command = initialize).pack(side=LEFT,padx=5,pady=5)
	Button(Mafenetre, text ='Quit', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

	w = Label(Mafenetre, text='     Costs: ', fg=myblack,font = "Verdana "+str(int(5*zoom))+" bold")
	w.pack(side=LEFT,padx=5,pady=5) 
	wg = Label(Mafenetre, text=str(cost[1]),fg=mygreen,font = "Verdana "+str(int(5*zoom))+" bold")
	wg.pack(side=LEFT,padx=5,pady=5) 
	wb = Label(Mafenetre, text=str(cost[2]),fg=myblue,font = "Verdana "+str(int(5*zoom))+" bold")
	wb.pack(side=LEFT,padx=5,pady=5) 
	wr = Label(Mafenetre, text=str(cost[3]),fg=myred,font = "Verdana "+str(int(5*zoom))+" bold")
	wr.pack(side=LEFT,padx=5,pady=5) 
	wn = Label(Mafenetre, text=str(cost[4]),fg=myblack,font = "Verdana "+str(int(5*zoom))+" bold")
	wn.pack(side=LEFT,padx=5,pady=5) 
	ws = Label(Mafenetre, text='     total = '+str(cost[0]),fg=myblack,font = "Verdana "+str(int(5*zoom))+" bold")
	ws.pack(side=LEFT,padx=5,pady=5) 
	Mafenetre.mainloop()