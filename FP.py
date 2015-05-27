from Tkinter import *
import random

root = Tk()
root.title('Flappy Plane')
root.minsize(800,500)
root.config(bg='light blue')

canvas = Canvas(root,bg="light blue")
canvas.config(width=800,height=500)


planeimg = PhotoImage(file='Jet.gif')
towerimg = PhotoImage(file='wtc.gif')

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
rate = 1


speed = -5
spawnrate = 900
gravity = .5


def loss():
    root.destroy()
    
    loss = Tk()
    loss.title('You Lost!')
    loss.config(bg="light blue")
    
    l = Label(loss,text='You Lost! %s points!'% int(score),bg='light blue').pack()
    
    
    
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
        
        loss()
        
    
    
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
    height = random.randint(0,250)
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
    
    
    
    
    
    root.after(spawnrate,maketower)

maketower()

canvas.pack()
root.mainloop()
