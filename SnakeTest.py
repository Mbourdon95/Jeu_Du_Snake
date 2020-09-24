from tkinter import *
from random import *
 
def move():
    global x,y,pX,pY
    global Serpent
    can.delete('all')
    i=len(Serpent)-1
    j=0
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
        can.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] +15, Serpent[i][1]+15,outline='black', fill='Lime') 
        i=i-1
    can.create_oval(pX, pY, pX+10, pY+10, outline='white', fill='red')
   
    if moves  == 'left':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = 493
    elif moves  == 'right':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > 493:
            Serpent[0][0] = 0
    elif moves  == 'up':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = 493
    elif moves  == 'bottom':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > 493:
            Serpent[0][1] = 0
    can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+15, Serpent[0][1]+15,outline='black', fill='green')
    
    test()
    test()
    
    if flag != 0:
        fen.after(60, move)
 
def newGame():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    move()
 
def left(event):
    global moves
    moves = 'left'
 
def right(event):
    global moves
    moves = 'right'
 
def up(event):
    global moves
    moves = 'up'
 
def down(event):
    global moves
    moves = 'bottom'
    
def test():
    global pomme
    global x,y,pX,pY,dx,dy
    global Serpent
    if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:        
        if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
            
            #On remet une pomme au hasard
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            can.coords(pomme,pX, pY, pX+5, pY+5)
            
            # On limite la Vitesse maximum du Serpent
            if dx > 18:
                dx +=0
                dy +=0
            else:
                dx += 0.5
                dy += 0.5
                
            #On ajoute un nouveau point au serpent
            Serpent.append([0,0])

# Position initial du Serpent.
# vitesse initial du Serpent

x = 245
y = 24        
dx, dy = 4, 4
flag = 0
moves = 'haut'
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]

pX = randrange(15, 485)
pY = randrange(15, 485)

# Création d'un Canva pour la gestion graphique
fen = Tk()
can = Canvas(fen, width=500, height=500, bg='gray')
can.pack(side=TOP, padx=5, pady=5) 

Corps_initial_Serpent =can.create_oval(Serpent[1][0], Serpent[1][1], Serpent[1][0] +15, Serpent[1][1]+15, outline='green', fill='red')
Tete_Initial_Serpent = can.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+15, Serpent[0][1]+15, outline='green', fill='green')
pomme = can.create_oval(pX, pY, pX+10, pY+10, outline='black', fill='white')

# Ajout de Boutton

btn_Play = Button(fen, text='Play', command=newGame, bg='white' , fg='black')
btn_Play.pack(side=LEFT, padx=100, pady=5)

btn_Exit = Button(fen, text='Exit', command=fen.destroy, bg='white' , fg='black')
btn_Exit.pack(side=RIGHT, padx=100, pady =5)

tex1 = Label(fen, text="Click on ' Play ' to Start", bg='white' , fg='black')
tex1.pack(padx=0, pady=5)

# Ajout des Contrôles

fen.bind('<z>' , up)
fen.bind('<s>', down)
fen.bind('<d>', right)
fen.bind('<q>', left)

    
fen.mainloop()
