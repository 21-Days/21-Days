import main
import menu_sl
import menu_options
from tkinter import *

def Save():
	root=tkinter.Tk()
	labels=saveload.labels(False)
	Slot1=Button(root, text=labels[1], command=saveload.save(1))
	Slot1.grid(row=1,column=0)
	Slot2=Button(root, text=labels[2], command=saveload.save(2))
	Slot2.grid(row=2,column=0)
	Slot3=Button(root, text=labels[3], command=saveload.save(3))
	Slot3.grid(row=3,column=0)
	Slot4=Button(root, text=labels[4], command=saveload.save(4))
	Slot4.grid(row=4,column=0)
def Load():
	root=tkinter.Tk()
	labels=saveload.labels(True)
	Heading=Label(root, text=labels[0])
	Slot0=Button(root, text=labels[1], command=saveload.save(0))
	Slot0.grid(row=1,column=0)
	Slot1=Button(root, text=labels[2], command=saveload.save(1))
	Slot1.grid(row=2,column=0)
	Slot2=Button(root, text=labels[3], command=saveload.save(2))
	Slot2.grid(row=3,column=0)
	Slot3=Button(root, text=labels[4], command=saveload.save(3))
	Slot3.grid(row=4,column=0)
	Slot4=Button(root, text=labels[5], command=saveload.save(4))
	Slot4.grid(row=5,column=0)
def options():
	print("Undeveloped")
def ingame():
	root=tkinter.tk()
	print("This is the Menu.")
	Label(root,text="This is the Menu").grid(row=0,column=0)
	Button(root,text="Resume Game", command=main.resume())
	Button(root,text="Save Game",command=save())
	Button(root,text="Load Game",command=load())
	Button(root,text="Options",command=options())
