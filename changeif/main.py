from tkinter import *
from recherche_policy import *
import numpy as np
import time
import matplotlib.pyplot as plt
from pl_policy import *
from minmax import *

def check_up(cj,li):
	if li>0:
		if g[li-1,cj][0]>0 :
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
	cu = check_up(cj,li)
	cd = check_down(cj,li)
	cl = check_left(cj,li-1)
	cr = check_right(cj,li-1)
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
				PosY -= zoom*20
				PosX += zoom*20
				cost[g[li-1,cj+1,0]]+=g[li-1,cj+1,1] 
			else:
				PosY -= zoom*20
				PosX -= zoom*20
				cost[g[li-1,cj-1,0]]+=g[li-1,cj-1,1] 
		elif cl and not cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
			else:
				PosY -= zoom*20
				PosX -= zoom*20
				cost[g[li-1,cj-1,0]]+=g[li-1,cj-1,1] 
		elif not cl and cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY -= zoom*20
				cost[g[li-1,cj,0]]+=g[li-1,cj,1]
			else:
				PosY -= zoom*20
				PosX += zoom*20
				cost[g[li-1,cj+1,0]]+=g[li-1,cj+1,1] 

def move_proba_down(cj, li):
	global PosX,PosY,cost,g
	cu = check_up(cj,li)
	cd = check_down(cj,li)
	cl = check_left(cj,li+1)
	cr = check_right(cj,li+1)
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
				PosY += zoom*20
				PosX += zoom*20
				cost[g[li+1,cj+1,0]]+=g[li+1,cj+1,1] 
			else:
				PosY += zoom*20
				PosX -= zoom*20
				cost[g[li+1,cj-1,0]]+=g[li+1,cj-1,1] 
		elif cl and not cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 
			else:
				PosY += zoom*20
				PosX -= zoom*20
				cost[g[li+1,cj-1,0]]+=g[li+1,cj-1,1] 
		elif not cl and cr:
			p0 = (proba+1)/2
			if p < p0:
				PosY += zoom*20
				cost[g[li+1,cj,0]]+=g[li+1,cj,1] 
			else:
				PosY += zoom*20
				PosX += zoom*20
				cost[g[li+1,cj+1,0]]+=g[li+1,cj+1,1] 

def move_proba_right(cj, li):
	global PosX,PosY,cost,g
	cu = check_up(cj+1,li)
	cd = check_down(cj+1,li)
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
				PosX += zoom*20
				PosY += zoom*20
				cost[g[li+1,cj+1,0]]+=g[li+1,cj+1,1] 
			else:
				PosX += zoom*20
				PosY -= zoom*20
				cost[g[li-1,cj+1,0]]+=g[li-1,cj+1,1]
		elif cu and not cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 
			else:
				PosX += zoom*20
				PosY -= zoom*20
				cost[g[li-1,cj+1,0]]+=g[li-1,cj+1,1]
		elif not cu and cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX += zoom*20
				cost[g[li,cj+1,0]]+=g[li,cj+1,1] 
			else:
				PosX += zoom*20
				PosY += zoom*20
				cost[g[li+1,cj+1,0]]+=g[li+1,cj+1,1] 

def move_proba_left(cj, li):
	global PosX,PosY,cost,g
	cu = check_up(cj-1,li)
	cd = check_down(cj-1,li)
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
				PosX -= zoom*20
				PosY += zoom*20
				cost[g[li+1,cj-1,0]]+=g[li+1,cj-1,1] 
			else:
				PosX -= zoom*20
				PosY -= zoom*20
				cost[g[li-1,cj-1,0]]+=g[li-1,cj-1,1]
		elif cu and not cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
			else:
				PosX -= zoom*20
				PosY -= zoom*20
				cost[g[li-1,cj-1,0]]+=g[li-1,cj-1,1]
		elif not cu and cd:
			p0 = (proba+1)/2
			if p < p0:
				PosX -= zoom*20
				cost[g[li,cj-1,0]]+=g[li,cj-1,1] 
			else:
				PosX -= zoom*20
				PosY += zoom*20
				cost[g[li+1,cj-1,0]]+=g[li+1,cj-1,1] 

def initialize():
	global PosX,PosY,cost
# position initiale du robot
	PosX = 20+10*zoom
	PosY = 20+10*zoom
	for k in range(6):
		cost[k]=0
# cout et affichage
	Canevas.coords(Pion,PosX -9*zoom, PosY -9*zoom, PosX +9*zoom, PosY +9*zoom)
	wg.config(text=str(cost[1]))
	wb.config(text=str(cost[2]))
	wr.config(text=str(cost[3]))
	wn.config(text=str(cost[4]))
	ws.config(text='     total = '+str(cost[0]))

def display_policy():
	window = Tk()
	window.title("Politique Total")
	cv = Canvas(window, width = Largeur, height =Hauteur, bg =mywhite)
	for i in range(nblignes):
		for j in range(nbcolonnes):          
			y =zoom*20*i+20
			x =zoom*20*j+20
			if g[i,j,0]>0:       
				#Canevas.create_oval(x+zoom*(10-3),y+zoom*(10-3),x+zoom*(10+3),y+zoom*(10+3),width=1,outline=color[g[i,j]],fill=color[g[i,j]])
				if type(policy[i][j]) is not np.array:
					if policy[i][j]==0:
						action_policy = '↑'
					elif policy[i][j]==1:
						action_policy = '↓'
					elif policy[i][j]==2:
						action_policy = '←'
					elif policy[i][j]==3:
						action_policy = '→'
				else:
					index = np.argmax(policy[i][j])
					if index==0:
						action_policy = 'p↑'
					elif index==1:
						action_policy = 'p↓'
					elif index==2:
						action_policy = 'p←'
					elif index==3:
						action_policy = 'p→'

				cv.create_text(x+zoom*(10),y+zoom*(10), text=action_policy,fill=mygreen,font = "Verdana "+str(int(6*zoom))+" bold")
			else:
				cv.create_rectangle(x, y, x+zoom*20, y+zoom*20, fill=mywalls)
	for i in range(nblignes+2):
		ni=zoom*20*i+20
		cv.create_line(20, ni, Largeur-20,ni)
	for j in range(nbcolonnes+2):
		nj=zoom*20*j+20
		cv.create_line(nj, 20, nj, Hauteur-20)
	cv.focus_set()
	cv.pack(padx =5, pady =5)
	window.mainloop()


	


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
	if touche == 'space':
		if type(policy[li][cj]) is not np.array:
			if policy[li][cj]==0:
				move_proba_up(cj, li)
			elif policy[li][cj]==1:
				move_proba_down(cj, li)
			elif policy[li][cj]==2:
				move_proba_left(cj, li)
			elif policy[li][cj]==3:
				move_proba_right(cj, li)
		else:
			p_up = policy[li][cj][0]
			p_down = policy[li][cj][1]
			p_left = policy[li][cj][2]
			p_right = policy[li][cj][3]
			p = np.random.uniform(0,1)
			
			if p <= p_up:
				move_proba_up(cj, li)
			elif p<= p_up + p_down:
				move_proba_down(cj, li)
			elif p<= p_up + p_down + p_left:
				move_proba_left(cj, li)
			elif p<= p_up + p_down + p_left + p_right:
				move_proba_right(cj, li)
			
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


def colordraw(g,nblignes,nbcolonnes, _display=True):
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
	if _display:
		for i in range(nblignes):
			for j in range(nbcolonnes):          
				y =zoom*20*i+20
				x =zoom*20*j+20
				if g[i,j,0]>0:            
					#Canevas.create_oval(x+zoom*(10-3),y+zoom*(10-3),x+zoom*(10+3),y+zoom*(10+3),width=1,outline=color[g[i,j]],fill=color[g[i,j]])
					Canevas.create_text(x+zoom*(10),y+zoom*(10), text=str(g[i,j,1]),fill=color[g[i,j,0]],font = "Verdana "+str(int(6*zoom))+" bold")
				else:
					Canevas.create_rectangle(x, y, x+zoom*20, y+zoom*20, fill=mywalls)
	set_objectif(g,nblignes, nbcolonnes, 1000, _display)
	#print("GGG",g)

def set_objectif(g, nblignes,nbcolonnes, _value_objectif, _display):
	global value_objectif
	value_objectif = _value_objectif
	i = nblignes-1
	j = nbcolonnes-1
	g[i, j, 0] = 5
	g[i, j, 1] = value_objectif
	if _display:
		y =zoom*20*i+20
		x =zoom*20*j+20
		Canevas.create_rectangle(x, y, x+zoom*20, y+zoom*20,  fill=myred)



def set_parameters(nbligness , nbcolonness, probas, weights):
	global nblignes , nbcolonnes, proba, weight
	nblignes = nbligness
	nbcolonnes = nbcolonness
	proba = probas
	weight = np.zeros(6, dtype=np.int)
	weight[1] = weights[1]
	weight[2] = weights[2]
	weight[3] = weights[3]
	weight[4] = weights[4]
	weight[5] = weights[5]


def init_game(_nblignes , _nbcolonness, _proba, _weight, _zoom=2, _PosX=20, _PosY=20, _gamma=0.9, _display=True, _q=1, _color=False, _optimizer=0):
	global g, cost, Pion, zoom, PosX, PosY, Canevas, policy, Largeur, Hauteur, times_list, iterations_list, valeurs_list, times_list2, valeurs_list2
	global color, myred, mygreen, myblue, mygrey, myyellow, myblack, mywalls, mywhite, w, wg, wb, wr, wn, ws

	set_parameters(_nblignes , _nbcolonness, _proba, _weight)
	gamma = _gamma
	zoom = _zoom
	PosX = _PosX
	PosY = _PosY

	if _display:
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
		cost= np.zeros(6, dtype=np.int)

		

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
		Pion = Canevas.create_oval(PosX -9*zoom, PosY -9*zoom, PosX +9*zoom, PosY +9*zoom,width=2,outline='black',fill=myyellow)
		Canevas.focus_set()
		Canevas.bind('<Key>',Clavier)
		Canevas.pack(padx =5, pady =5)

		if (_optimizer==0):
			policy, iteration = itervalue(g, nblignes, nbcolonnes, proba, gamma , e=0.0001, objectif=value_objectif, _q=_q, _color=_color)
		elif (_optimizer==1):
			g1=change_grill(g,nblignes, nbcolonnes,value_objectif)
			policy=optimalepure(nblignes, nbcolonnes,4 , g1,proba, gamma)
		elif (_optimizer==2):
			g1=change_grill(g,nblignes, nbcolonnes,value_objectif)
			policy=optimale(nblignes, nbcolonnes,4 , g1,proba, gamma)
		# Craation d'un widget Button (bouton Quitter)
		# Creation d'un widget Button (bouton Quitter)
		Button(Mafenetre, text ='Restart', command = initialize).pack(side=LEFT,padx=5,pady=5)
		Button(Mafenetre, text ='Quit', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)
		Button(Mafenetre, text ='Policy', command = display_policy).pack(side=LEFT,padx=5,pady=5)

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

	else:
		# valeurs de la grille
		g = np.zeros((nblignes,nbcolonnes,2), dtype=np.int)
		cost= np.zeros(6, dtype=np.int)
		colordraw(g,nblignes,nbcolonnes,_display)
		t0 = time.time()
		if (_optimizer==0):
			policy, iteration = itervalue(g, nblignes, nbcolonnes, proba, gamma , e=0.0001, objectif=value_objectif, _q=_q, _color=_color)
			t1 = time.time()
			times_list.append(t1-t0)
			iterations_list.append(iteration)
		elif (_optimizer==1):
			g1=change_grill(g,nblignes, nbcolonnes,value_objectif)
			policy=optimalepure(nblignes, nbcolonnes,4 , g1,proba, gamma)
			t1 = time.time()
			times_list.append(t1-t0)
		elif (_optimizer==2):
			g1=change_grill(g,nblignes, nbcolonnes,value_objectif)
			policy=optimale(nblignes, nbcolonnes,4 , g1,proba, gamma)
			t1 = time.time()
			times_list.append(t1-t0)
		#_optimizer==3 est fait que pour la question 3C
		elif (_optimizer==3):
			g1=change_grill(g,nblignes, nbcolonnes,value_objectif)
			policy, valeur=optimalepure(nblignes, nbcolonnes,4 , g1,proba, gamma)
			t1 = time.time()
			times_list.append(t1-t0)
			valeurs_list.append(valeur)
			t2 = time.time()
			g2=change_grill(g,nblignes, nbcolonnes,value_objectif)
			policy, valeur2=optimale(nblignes, nbcolonnes,4 , g1,proba, gamma)
			t3 = time.time()
			times_list2.append(t3-t2)
			valeurs_list2.append(valeur2)

def comparer_make_images():
	global times_list, iterations_list
	_weight = [0,1,2,3,4,-1]

	times_list=[]
	iterations_list=[]
	times_mean=[]
	iterations_mean=[]
	for p in [1,0.6]:
		for nbl,nbc in [[10,10],[10,15],[15,20]]:
			y_time = []
			y_iter = []
			for g in [0.9,0.7,0.5]:
				times_list=[]
				iterations_list=[]
				for i in range(15):
					init_game(nbl , nbc, _proba=p, _weight=_weight, _gamma=g, _display=False)
				times_mean.append(np.mean(np.array(times_list)))
				iterations_mean.append(np.mean(np.array(iterations_list)))
				y_time.append(np.mean(np.array(times_list)))
				y_iter.append(np.mean(np.array(iterations_list)))
			x = [0.9,0.7,0.5]
			ln1, = plt.plot(x, y_time, color='red')
			plt.legend(handles=[ln1],labels=['time mean'])
			plt.title("Moyenne de temps")
			plt.savefig('./Results/'+str(p)+"_"+str(nbl)+"mult"+str(nbc)+"_time.jpg")
			plt.xlabel("Different gamma")
			plt.ylabel("Time mean")
			plt.show()
			ln2, = plt.plot(x, y_iter, color='blue')
			plt.legend(handles=[ln2],labels=['iteration mean'])
			plt.title("Moyenne d'itérations")
			plt.savefig('./Results/'+str(p)+"_"+str(nbl)+"mult"+str(nbc)+"_iter.jpg")
			plt.xlabel("Different gamma")
			plt.ylabel("Iteration mean")
			plt.show()

def comparer_make_image_3c():
	global times_list, valeurs_list, times_list2, valeurs_list2
	_weight = [0,1,2,3,4,-1]
	nbl,nbc = 10,15
	for p in [1,0.6]:
		times_mean=[]
		valeurs_mean=[]
		times_mean2=[]
		valeurs_mean2=[]
		for g in [0.9,0.7,0.5]:
			times_list=[]
			valeurs_list=[]
			times_list2=[]
			valeurs_list2=[]
			for i in range(15):
				init_game(nbl , nbc, _proba=p, _weight=_weight, _gamma=g, _display=False, _optimizer=3)
			times_mean.append(np.mean(np.array(times_list)))
			valeurs_mean.append(np.mean(np.array(valeurs_list)))
			times_mean2.append(np.mean(np.array(times_list2)))
			valeurs_mean2.append(np.mean(np.array(valeurs_list2)))

		x = [0.9,0.7,0.5]

		ln1, = plt.plot(x, times_mean, color='red')
		ln2, = plt.plot(x, times_mean2, color='green')
		plt.legend(handles=[ln1,ln2],labels=['time mean pure','time mean mixte'])
		plt.title("Moyenne de temps")
		plt.savefig('./Results/3C/'+str(p)+"_"+str(nbl)+"mult"+str(nbc)+"_time.jpg")
		plt.xlabel("Different gamma")
		plt.ylabel("Time mean")
		plt.show()
		ln3, = plt.plot(x, valeurs_mean, color='red')
		ln4, = plt.plot(x, valeurs_mean2, color='green')
		plt.legend(handles=[ln3,ln4],labels=['value mean pure','value mean mixte'])
		plt.title("Moyenne de valeurs")
		plt.savefig('./Results/3C/'+str(p)+"_"+str(nbl)+"mult"+str(nbc)+"_valeurComparaison.jpg")
		plt.xlabel("Different gamma")
		plt.ylabel("Value mean")
		plt.show()

		ln3, = plt.plot(x, valeurs_mean, color='red')
		plt.legend(handles=[ln3],labels=['value mean mixte'])
		plt.title("Moyenne de valeurs")
		plt.savefig('./Results/3C/'+str(p)+"_"+str(nbl)+"mult"+str(nbc)+"_valeurPure.jpg")
		plt.xlabel("Different gamma")
		plt.ylabel("Value mean")
		plt.show()

		ln4, = plt.plot(x, valeurs_mean2, color='green')
		plt.legend(handles=[ln4],labels=['value mean mixte'])
		plt.title("Moyenne de valeurs")
		plt.savefig('./Results/3C/'+str(p)+"_"+str(nbl)+"mult"+str(nbc)+"_valeurMixte.jpg")
		plt.xlabel("Different gamma")
		plt.ylabel("Value mean")
		plt.show()

if __name__ == "__main__":

	#question 2b
	#comparer_make_images()

	#question 2c
	_nblignes = 10
	_nbcolonness = 15
	_proba = 0.8
	_weight = [0,1,2,3,4,-1]
	_gamma = 0.9
	_display = True
	_q = 5
	_color = False
	#init_game(_nblignes , _nbcolonness, _proba=_proba, _weight=_weight, _gamma=_gamma, _display=_display, _q=_q, _color=_color)

	#question 2d
	#_color = True
	#init_game(_nblignes , _nbcolonness, _proba=_proba, _weight=_weight, _gamma=_gamma, _display=_display, _q=_q, _color=_color)

	#question 3c
	comparer_make_image_3c()

	

