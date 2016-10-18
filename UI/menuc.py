import main
import menu
import function
from tkinter import *

def Save():
	function.clear()
	root=tkinter.Tk()
	labels=saveload.labels(False)
	Button(root, text=labels[1], command=saveload.save(1)).grid(row=1,column=0)
	Button(root, text=labels[2], command=saveload.save(2)).grid(row=2,column=0)
	Button(root, text=labels[3], command=saveload.save(3)).grid(row=3,column=0)
	Button(root, text=labels[4], command=saveload.save(4)).grid(row=4,column=0)
def Load():
	function.clear()
	root=tkinter.Tk()
	labels=saveload.labels(True)
	Label(root, text=labels[0]).grid(row=0,column=0)
	Button(root, text=labels[1], command=saveload.save(0)).grid(row=1,column=0)
	Button(root, text=labels[2], command=saveload.save(1)).grid(row=2,column=0)
	Button(root, text=labels[3], command=saveload.save(2)).grid(row=3,column=0)
	Button(root, text=labels[4], command=saveload.save(3)).grid(row=4,column=0)
	Button(root, text=labels[5], command=saveload.save(4)).grid(row=5,column=0)
def options():
	print("Undeveloped")
def confirm():
	function.clear()
	root=tkinter.tk()
	Label(root,text="Are you sure?").grid(row=0,column=0)
	Button(root,text="Yes",command=menu.main()).grid(row=1,column=0)
	Button(root,text="No",command=menu.ingame()).grid(row=2,column=0)
	
