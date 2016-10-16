from tkinter import *
import menuc

def main():

def ingame():
	root=tkinter.tk()
	print("This is the Menu.")
	Label(root,text="This is the Menu").grid(row=0,column=0)
	Button(root,text="Resume Game", command=main.resume()).grid(row=1,column=0)
	Button(root,text="Save Game",command=menuc.save()).grid(row=2,column=0)
	Button(root,text="Load Game",command=menuc.load()).grid(row=3,column=0)
	Button(root,text="Options",command=menuc.options()).grid(row=4,column=0)
	Button(root,text="Quit",command=menuc.confirmquit()).grid(row=5,column=0)
