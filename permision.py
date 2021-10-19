from functools import partial
from tkinter import *
from tkinter import *
import PIL
from subprocess import Popen
p=Popen("python videorecording.py")
i=0
def test():
    #print("tst")
    root.destroy()
    from  g1test import  quiz
    quiz
    p.kill()
def switch1():
    if C1["state"] == "disabled" and C2["state"] == "disabled" and C3["state"] == "disabled" and  C4["state"] == "disabled":
        start = Button(frame, text="Start TEST", command=test, bg='red').place(x=180, y=500)


def checkaudio():
    C1.configure(frame,variable=2,state=DISABLED)
    switch1()
    p2 = Popen("python audio.py")

def checkvidio():
    C2.configure(frame,variable=2,state=DISABLED)
    switch1()
    return True

def checknetwork():
    C3.configure(frame, variable=2, state=DISABLED)
    switch1()
    return True


def checklocation():
    C4.configure(frame, variable=2, state=DISABLED)
    switch1()
    return True
root = Tk()
root.attributes('-fullscreen',True)
root.configure(bg='#fff')
frame = Frame(root,width=350, height=500,bg='#f0f8ff').place(x=10,y=100)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
title = Label(frame, text="Prerequisite", width=100, bg="blue",fg="white", font=("ariel", 20, "bold"))
C1 = Checkbutton(frame, text = "Audio", variable = CheckVar1,onvalue = 1, offvalue = 0,bg='#f0f8ff')
C2 = Checkbutton(frame, text = "Video", variable = CheckVar2,onvalue = 1, offvalue = 0,bg='#f0f8ff')
C3 = Checkbutton(frame, text = "Network", variable = CheckVar3,onvalue = 1, offvalue = 0,bg='#f0f8ff')
C4 = Checkbutton(frame, text = "Location", variable = CheckVar4,onvalue = 1, offvalue = 0,bg='#f0f8ff' )
C1.place(x=20,y=100)
C2.place(x=20,y=150)
C3.place(x=20,y=200)
C4.place(x=20,y=250)
title.place(x=0, y=2)
canvas = Canvas(root, width =1450, height =1000)
canvas.place(x=275,y=40)
img = PIL.ImageTk.PhotoImage(PIL.Image.open("pem.jpg"))
canvas.create_image(500,275, image=img)
button=Button(frame,text="Start",command=checkaudio).place(x=180,y=100)
button2=Button(frame,text="Start",command=checkvidio).place(x=180,y=150)
button3=Button(frame,text="Start",command=checknetwork).place(x=180,y=200)
button4=Button(frame,text="Start",command=checklocation).place(x=180,y=250)
root.mainloop()
