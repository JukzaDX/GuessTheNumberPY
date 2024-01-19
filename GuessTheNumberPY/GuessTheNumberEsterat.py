from tkinter.ttk import *
from tkinter import *
import random

win = Tk()
win.config(background='#003049')

Tries = 0

def close():
    win.destroy()

def Randomness(*args):
    global rng
    global Tries
    Ent.config(state='normal')
    Tries = 0
    Trlbl.config(text="Tries:"+ str(Tries))
    if rb.get() == "Easy":
        rng = random.randint(1,100)
    elif rb.get() == "Medium":
        rng = random.randint(1,250)
    elif rb.get() == "Hard":
        rng = random.randint(1,500)


def Game(event):
    global Tries
    Tries += 1
    Trlbl.config(text="Tries:" + str(Tries))

    if int(Ent.get()) > rng:
        Imglbl.config(image=GreenDown)
        Ent.delete(0, END)
        RngBtn.config(state='disabled')
    elif int(Ent.get()) < rng:
        Imglbl.config(image=GreenUp)
        Ent.delete(0, END)
        RngBtn.config(state='disabled')
    elif int(Ent.get()) == rng:
        Imglbl.config(image=Check)
        Ent.delete(0,END)
        Ent.config(state='disabled')
        RngBtn.config(state='active')

rb = StringVar()
rb.trace("w", Randomness)



tilbl = Label(win,text="Guess The Number",font=('Calibri',36),borderwidth=10,relief='ridge')
tilbl.config(foreground='#fdf0d5',background='#003049')
tilbl.grid(row=1,column=0)

Inlbl = Label(win,text="Select A Difficulty, Press Randomise And Then Guess!",font=('Calibri',22),borderwidth=6,relief='ridge')
Inlbl.config(foreground='#fdf0d5',background='#003049')
Inlbl.place(x=0,y=125)

Ezrad = Radiobutton(win,text="Easy(1-100)",value="Easy", var=rb)
Ezrad.place(x=0,y=90)

Mdrad = Radiobutton(win,text="Medium(1-250)",value="Medium",var=rb)
Mdrad.place(x=100,y=90)

Hrdrad = Radiobutton(win,text="Hard(1-500)",value="Hard",var=rb)
Hrdrad.place(x=225,y=90)

Trlbl = Label(win,text="Tries:",font=('Calibri',18),borderwidth=4,relief='ridge')
Trlbl.config(foreground='#fdf0d5',background='#003049')
Trlbl.place(x=0,y=175)

Ent = Entry(win,font=('Arial',15))
Ent.place(x=120,y=180)

RngBtn = Button(win,text="Randomise",font=('Calibri',16),command = Randomness)
RngBtn.place(x=0,y=225)

Exbtn = Button(win,text="Exit",font=('Calibri',14))
Exbtn.bind(close)
Exbtn.place(x=0,y=275)

Dice = PhotoImage(file='dice.png')
GreenUp = PhotoImage(file='GreenUp.png')
GreenDown = PhotoImage(file='GreenDown.png')
RedUp = PhotoImage(file='RedUp.png')
RedDown = PhotoImage(file='RedDown.png')
Check = PhotoImage(file='Check.png')

Imglbl = Label(win,image=Dice,bg='#003049')
Imglbl.place(x=125,y=220)

win.bind('<Return>', Game)

win.geometry('635x630')
win.mainloop()