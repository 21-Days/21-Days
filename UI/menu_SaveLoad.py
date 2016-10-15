from tkinter import *
import saveload

def Save():
	root=Tk()
	labels=saveload.labels(False)
	Slot1=Button(root, text=labels[1], command=saveload.save(1))
	Slot2=Button(root, text=labels[2], command=saveload.save(2))
	Slot3=Button(root, text=labels[3], command=saveload.save(3))
	Slot4=Button(root, text=labels[4], command=saveload.save(4))
	
