import gui
import function
import webbrowser
from tkinter import *

def Save(root,main):
	function.clear(root)
	labels=saveload.labels(False)
	Button(root, text=labels[1], command=saveload.save(1)).grid(row=1,column=0)
	Button(root, text=labels[2], command=saveload.save(2)).grid(row=2,column=0)
	Button(root, text=labels[3], command=saveload.save(3)).grid(row=3,column=0)
	Button(root, text=labels[4], command=saveload.save(4)).grid(row=4,column=0)
	if(main==True):
		Button(root, text="Back", command=gui.main()).grid(row=5,column=0)
	else:
		Button(root, text="Back", command=gui.ingame()).grid(row=5,column=0)
def Load(root,main):
	function.clear()
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
	if(main==True):
		Button(root, text="Back", command=gui.main()).grid(row=6,column=0)
	else:
		Button(root, text="Back", command=gui.ingame()).grid(row=6,column=0)
def credits(root, main):
	function.clear(root)
	Label(root, text="Credits", font=32).grid(row=0,column=0)
	Label(root, text="Programmer: Roadkillsanta (EN)", font=16).grid(row=1,column=0)
	Label(root, text="Programmer: BOOMCHICKEN (JZ)", font=16).grid(row=4,column=0)
	Label(root, text="Writer: GoobysTheName (WJ)", font=16).grid(row=3,column=0)
	Label(root, text="Writer: BOOMCHICKEN (JZ)", font=16).grid(row=4,column=0)
	Button(root, text="@RGTN (github.com/RGTN)", font=16, command=webbrowser.open("http:github.com/RGTN", new=2, autoraise=True)).grid(row=5,column=0)
	Label(root, text="Special Thanks: GitHub (github.com)", font=16).grid(row=6,column=0)
	Label(root, text="", font=16).grid(row=7,column=0)
	if(main==True):
		Button(root, text="Back", font=16, command=gui.main()).grid(row=8,column=0)
	else:
		Button(root, text="Back", font=16, command=gui.ingame()).grid(row=8,column=0)
def confirm(root,main):
	function.clear(root)
	Label(root,text="Are you sure?").grid(row=0,column=0, columnspan=2)
	if(main==True):
		Button(root,text="Yes",command=gui.exit()).grid(row=1,column=0)
		Button(root,text="No",command=gui.main()).grid(row=1,column=1)
	else:
		Button(root,text="Yes",command=gui.main()).grid(row=1,column=0)
		Button(root,text="No",command=gui.ingame()).grid(row=1,column=1)
	
	
