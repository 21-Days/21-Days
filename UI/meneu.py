from tkinter import *
import menu

def main():

def ingame():
	root=tkinter.tk()
	print("This is the Menu.")
	Label(root,text="This is the Menu").grid(row=0,column=0)
	Button(root,text="Resume Game", command=main.resume())
	Button(root,text="Save Game",command=menu.save())
	Button(root,text="Load Game",command=menu.load())
	Button(root,text="Options",command=menu.options())
