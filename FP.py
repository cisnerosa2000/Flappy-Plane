from Tkinter import *
import random
import math

root = Tk()
root.title('Flappy Plane')
root.minsize(800,500)
root.config(bg='light blue')

canvas = Canvas(root,bg="light blue")
canvas.config(width=800,height=500)


planeimg = PhotoImage(file='Jet.gif')
towerimg = PhotoImage(file='wtc.gif')
crashimg = PhotoImage(file='Crash.gif')

plane = canvas.create_image(400,200,image=planeimg)

text = Text(root)
text.config(width=100,height=1,bg='light blue')
text.insert(INSERT,'Score:')
text.config(state=DISABLED)
text.pack()

global score
score = 0

global rate
global speed
global spawnrate
global gravity
global key
global lost

rate = 1
lost = False
key = ''
speed = -5
spawnrate = 900
gravity = .5



class Encryption(object):
    def __init__(self,encryptme,decryptme):
        self.encryptme = encryptme
        self.decryptme = decryptme
        
    def encrypt(self):
        global key
        for emptyspace in range(0,10):
           emptyspace = random.randint(0,9)
           key += str(emptyspace)
    
    
        score2 = self.encryptme ** 2
        score3 = str(score2)[::-1]
 
        return str(key) + str(key).join(str(score3))
    def decrypt(self):
        tbd = self.decryptme
        oldkey = (tbd[0]+ tbd[1] + tbd[2] + tbd[3] + tbd[4]+ tbd[5]+ tbd[6]+ tbd[7]+ tbd[8]+ tbd[9])
        
        newtbd = tbd.split(oldkey)
        newtbd = "".join(newtbd)

        decoded = newtbd.split(oldkey)
        decoded = "".join(decoded)
        
        decoded2 = decoded[::-1]
        return math.sqrt(int(decoded2))

def loss():
    root.destroy()
    
    loss = Tk()
    loss.title('You Lost!')
    loss.config(bg="light blue")
    
    
    def highscore_():
        global score_snapshot
        with open('flappy_score.txt','r') as read_old_score:
            
            decryptsoon = read_old_score.read()
            doody = Encryption(decryptme=decryptsoon,encryptme="Ignore Me!")
            highest_score = doody.decrypt()
            
            
            
            
           
        
        if score_snapshot > float(highest_score):
            with open('flappy_score.txt','w') as new_high_score:
                poopy = Encryption(encryptme = int(score_snapshot),decryptme="Ignore Me!")
                new_high_score.write(poopy.encrypt())
                
                
            
        
        encryptedscore = Encryption(encryptme = score, decryptme = "Ignore please!")
    
    
    
        
        if score_snapshot > float(highest_score):
            loser = Label(loss,text="New high score of %s!" % (int(score_snapshot)),bg='light blue')
            loser.pack()
        else:
            loser2 = Label(loss,text="You got a score of %s! Your high score is %s" % (int(score_snapshot),int(highest_score)),bg='light blue')
            loser2.pack()
    
    
    
    highscore_()
   
   
   
    loss.mainloop()


def fall_loop():
    global score
    global rate
    global speed
    global spawnrate
    global gravity
    
    canvas.move(plane,0,rate)
    canvas.move("tower",speed,0)
     
    rate += gravity
    speed -= .02
    gravity += .0008
    
    if canvas.coords(plane)[1] >= 500 or canvas.coords(plane)[1] <= 0:
        loss()
    
    
    playerbbox = canvas.bbox(plane)
    overlap = canvas.find_overlapping(*playerbbox)
    
    
    
    text.config(state=NORMAL)
    text.delete(1.0,END)
    text.insert(INSERT,'Score: %s' % (int(score)) )
    text.config(state=DISABLED)
    
    
    
    if len(overlap) > 1:
        global score_snapshot
        global lost
        
        lost = True
        score_snapshot = score
        canvas.create_image(canvas.coords(plane)[0],canvas.coords(plane)[1],image=crashimg)
        canvas.delete(plane)   

        root.after(3000,loss)     
    
    if lost == False:
        root.after(1,fall_loop)
    
    
fall_loop()


def up(event):
    global rate
    
    rate = 0
    canvas.move(plane,0,-20)
    

def kill(event):
    root.destroy()
    
root.bind('<a>',up)
root.bind('<s>',up)
root.bind('<d>',up)
root.bind('<space>',up)







def maketower():
    global spawnrate
    global score
    global lost
    height = random.randint(100,250)
    initial_height = height
    
    for num in range(1,10):
        
        tower = canvas.create_image(700,height,image=towerimg,tags="tower")
        height -= 59
        
        tbd = canvas.addtag_overlapping("delete",0,-1000,300,1000)
        canvas.delete("delete")
        
        score += .11
        
    spawnrate -= 2
    

    
    tower2spawn = initial_height + random.randint(200,300)
    def hide():
        tower2 = canvas.create_image(700,tower2spawn,image=towerimg,tags="tower")
        a = canvas.create_image(700,tower2spawn+60,image=towerimg,tags="tower")
        b = canvas.create_image(700,tower2spawn+120,image=towerimg,tags="tower")
        c = canvas.create_image(700,tower2spawn+180,image=towerimg,tags="tower")
        d = canvas.create_image(700,tower2spawn+240,image=towerimg,tags="tower")
        e = canvas.create_image(700,tower2spawn+300,image=towerimg,tags="tower")
    hide()
    
    
    
    
    if lost == False:
        root.after(spawnrate,maketower)

maketower()

canvas.pack()
root.mainloop()
