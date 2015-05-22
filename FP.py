from Tkinter import *
import random

root = Tk()
root.title('Flappy Plane')
root.minsize(800,500)

canvas = Canvas(root,bg="light blue")
canvas.config(width=800,height=500)


planeimg = PhotoImage(file='Jet.gif')
towerimg = PhotoImage(file='wtc.gif')

plane = canvas.create_image(400,200,image=planeimg)

text = Text(root)
text.config(width=100,height=1)
text.insert(INSERT,'Score:')
text.config(state=DISABLED)
text.pack()

global score
score = 0

global rate
rate = 1

def fall_loop():
    global score
    global rate
    
    canvas.move(plane,0,rate)
    rate += .5
    canvas.move("tower",-5,0)
    
    playerbbox = canvas.bbox(plane)
    overlap = canvas.find_overlapping(*playerbbox)
    
    
    
    text.config(state=NORMAL)
    text.delete(1.0,END)
    text.insert(INSERT,'Score: %s' % (int(score)) )
    text.config(state=DISABLED)
    
    
    
    if len(overlap) > 1:
        root.destroy()
        
        loss = Tk()
        loss.title('You Lost!')
        
        l = Label(loss,text='You Lost! %s points!'% int(score)).pack()
        
        
        
        loss.mainloop()
    
    
    root.after(1,fall_loop)
    
    
fall_loop()


def up(event):
    global rate
    
    rate = 0
    canvas.move(plane,0,-20)

def kill(event):
    root.destroy()
    asdaa
root.bind('<a>',up)
root.bind('<s>',up)
root.bind('<d>',up)
root.bind('<space>',up)

root.bind('<Up>',kill)






def maketower():
    global score
    height = random.randint(0,250)
    initial_height = height
    
    for num in range(1,10):
        
        tower = canvas.create_image(700,height,image=towerimg,tags="tower")
        height -= 59
        
        tbd = canvas.addtag_overlapping("delete",0,-1000,300,1000)
        canvas.delete("delete")
        
        score += .11

    
    tower2spawn = initial_height + random.randint(200,300)
    def hide():
        tower2 = canvas.create_image(700,tower2spawn,image=towerimg,tags="tower")
        a = canvas.create_image(700,tower2spawn+60,image=towerimg,tags="tower")
        b = canvas.create_image(700,tower2spawn+120,image=towerimg,tags="tower")
        c = canvas.create_image(700,tower2spawn+180,image=towerimg,tags="tower")
        d = canvas.create_image(700,tower2spawn+240,image=towerimg,tags="tower")
        e = canvas.create_image(700,tower2spawn+300,image=towerimg,tags="tower")
    hide()
    
    
    
    
    
    root.after(800,maketower)

maketower()

canvas.pack()
root.mainloop()
