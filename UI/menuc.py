import gui
import function
from tkinter import *

def Save(root,main):
	function.clear(root)
	labels=saveload.labels(False)
	Button(root, text=labels[1], command=saveload.save(1)).grid(row=1,column=0)
	Button(root, text=labels[2], command=saveload.save(2)).grid(row=2,column=0)
	Button(root, text=labels[3], command=saveload.save(3)).grid(row=3,column=0)
	Button(root, text=labels[4], command=saveload.save(4)).grid(row=4,column=0)
	if(main=True):
		Button(root, text="Back", command=gui.main()).grid(row=5,column=0)
	else:
		Button(root, text="Back", command=gui.ingame()).grid(row=5,column=0)
def Load(root,main):
	function.clear()
	root=tkinter.Tk()
	labels=saveload.labels(True)
	Label(root, text=labels[0], font=32).grid(row=0,column=0)
	Button(root, text=labels[1], command=saveload.load(0)).grid(row=1,column=0)
	Button(root, text=labels[2], command=saveload.load(1)).grid(row=2,column=0)
	Button(root, text=labels[3], command=saveload.load(2)).grid(row=3,column=0)
	Button(root, text=labels[4], command=saveload.load(3)).grid(row=4,column=0)
	Button(root, text=labels[5], command=saveload.load(4)).grid(row=5,column=0)
	if(main=True):
		Button(root, text="Back", command=gui.main()).grid(row=6,column=0)
	else:
		Button(root, text="Back", command=gui.ingame()).grid(row=6,column=0)
def options(root,main):
	function.clear(root)
	Label(root, text="Options", font=32).grid(row=0,column=0)
	if(main=True):
		Button(root, text="Back", command=gui.main()).grid(row=6,column=0)
	else:
		Button(root, text="Back", command=gui.ingame()).grid(row=6,column=0)
def confirm(root):
	function.clear(root)
	root=tkinter.tk()
	Label(root,text="Are you sure?").grid(row=0,column=0)
	Button(root,text="Yes",command=gui.main()).grid(row=1,column=0)
	Button(root,text="No",command=gui.ingame()).grid(row=2,column=0)
	
