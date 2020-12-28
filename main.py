from tkinter import *
import numpy as np

def check_up(cj,li):
	if li>0:
		if g[li-1,cj]>0:
			return True
	return False

def check_down(cj,li):
	if li<nblignes-1:
		if g[li+1,cj]>0:
			return True
	return False

def check_right(cj,li):
	if cj<nbcolonnes-1:
		if g[li,cj+1]>0:
			return True
	return False

def check_left(cj,li):
	if cj>0:
		if g[li,cj-1]>0:
			return True
	return False

def move_proba(cj, li, action):
	global PosX,PosY
	cu = check_left(cj,li)
	cd = check_down(cj,li)
	cl = check_left(cj,li)
	cr = check_right(cj,li)
	if action=="up":
		if not cl and not cr:
			PosY -= 20
		else:
			p=np.random.uniform(0,1)
			if cl and cr:
				p0 = proba
				p1 = (1-proba)/2
				if p < p0:
					PosY -= 20
				elif p < p0+p1:
					PosX += 20
				else:
					PosX -= 20
			elif cl and not cr:
				p0 = (proba+1)/2
				if p < p0:
					PosY -= 20
				else:
					PosX -= 20
			elif not cl and cr:
				p0 = (proba+1)/2
				if p < p0:
					PosY -= 20
				else:
					PosX += 20
	elif action=="down":
		if not cl and not cr:
			PosY += 20
		else:
			p=np.random.uniform(0,1)
			if cl and cr:
				p0 = proba
				p1 = (1-proba)/2
				if p < p0:
					PosY += 20
				elif p < p0+p1:
					PosX += 20
				else:
					PosX -= 20
			elif cl and not cr:
				p0 = (proba+1)/2
				if p < p0:
					PosY += 20
				else:
					PosX -= 20
			elif not cl and cr:
				p0 = (proba+1)/2
				if p < p0:
					PosY += 20
				else:
					PosX += 20

	elif action=="right":
		if not cu and not cd:
			PosX += 20
		else:
			p=np.random.uniform(0,1)
			if cu and cd:
				p0 = proba
				p1 = (1-proba)/2
				if p < p0:
					PosX += 20
				elif p < p0+p1:
					PosY += 20
				else:
					PosY -= 20
			elif cu and not cd:
				p0 = (proba+1)/2
				if p < p0:
					PosX += 20
				else:
					PosY -= 20
			elif not cu and cd:
				p0 = (proba+1)/2
				if p < p0:
					PosX += 20
				else:
					PosY += 20

	elif action=="left":
		if not cu and not cd:
			PosX -= 20
		else:
			p=np.random.uniform(0,1)
			if cu and cd:
				p0 = proba
				p1 = (1-proba)/2
				if p < p0:
					PosX -= 20
				elif p < p0+p1:
					PosY += 20
				else:
					PosY -= 20
			elif cu and not cd:
				p0 = (proba+1)/2
				if p < p0:
					PosX -= 20
				else:
					PosY -= 20
			elif not cu and cd:
				p0 = (proba+1)/2
				if p < p0:
					PosX -= 20
				else:
					PosY += 20
	


def Clavier(event):
	global PosX,PosY
	touche = event.keysym
	cj=round((PosX-30)/20)
	li=round((PosY-30)/20)
	# print(li,cj)
	# deplacement vers le haut
	if touche == 'Up' and check_up(cj,li):
		move_proba(cj, li, 'up')
	# deplacement vers le bas
	if touche == 'Down' and check_down(cj,li):
		move_proba(cj, li, 'down')
	# deplacement vers la droite
	if touche == 'Right' and check_right(cj,li):
		move_proba(cj, li, 'right')
	# deplacement vers la gauche
	if touche == 'Left' and check_left(cj,li):
		move_proba(cj, li, 'left')
	# on dessine le pion a sa nouvelle position
	Canevas.coords(Pion,PosX -10, PosY -10, PosX +10, PosY +10)


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
				g[i,j]=c
				Canevas.create_oval(10+x-3,10+y-3,10+x+3,10+y+3,width=1,outline=color[c],fill=color[c])
			else:
				Canevas.create_rectangle(x, y, x+20, y+20, fill=myblack)
	print("GG",g)




if __name__ == "__main__":
	#taille de la grille
	nblignes=10
	nbcolonnes=15
	proba = 0.8


	Mafenetre = Tk()
	Mafenetre.title('MADI PROJET')

	# position initiale du pion
	PosX = 30
	PosY = 30

	# Creation d'un widget Canvas (zone graphique)
	Largeur = 20*nbcolonnes+40
	Hauteur = 20*nblignes+40
	 
	# valeurs de la grille
	g = np.zeros((nblignes,nbcolonnes), dtype=np.int)

	myred="#F70B42"
	mygreen="#1AD22C"
	myblue="#0B79F7"
	mygrey="#E8E8EB"
	myyellow="#F9FB70"
	myblack="#5E5E64"
	mywhite="#FFFFFF"

	color=[mywhite,mygreen,myblue,myred,myblack]

	Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg =mywhite)
	for i in range(nblignes+2):
	    ni=20*i
	    Canevas.create_line(20, ni, Largeur-20,ni)
	for j in range(nbcolonnes+2):
	    nj=20*j
	    Canevas.create_line(nj, 20, nj, Hauteur-20)
	colordraw(g,nblignes,nbcolonnes)
	Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2,outline='black',fill=myyellow)
	Canevas.focus_set()
	Canevas.bind('<Key>',Clavier)
	Canevas.pack(padx =5, pady =5)

	# Craation d'un widget Button (bouton Quitter)
	Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

	Mafenetre.mainloop()