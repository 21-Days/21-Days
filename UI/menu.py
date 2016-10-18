from tkinter import *
import menuc
import main
import function

def main():
	function.clear()
	root=tkinter.Tk()
	file=open("menutitles.txt","r")
	sub=file.readlines()
	Label(root,text="21 Days",font=32).grid(0,0)
	Label(root,text=sub[random.randint(0,15)],font=12).grid(row=1,column=0)
	Button(root,text="Play!",command=GUI_main.run()).grid(row=2,column=0)
	Button(root,text="",command=).grid(row=3,column=0)
	Button(root,text="Load Save",command=menuc.load()).grid(row=4,column=0)
	Button(root,text="Options",command=menuc.options()).grid(row=5,column=0)
	Button(root,text="Credits",command=menuc.credits()).grid(row=6,column=0)
	Button(root,text="Quit",command=main.exit()).grid(row=7,column=0)
def ingame():
	function.clear()
	root=tkinter.Tk()
	file=open("menutitles.txt","r")
	title=file.readlines()
	Label(root,text=title[random.randint(0,15)]).grid(row=0,column=0)
	Button(root,text="Resume Game", command=main.resume()).grid(row=1,column=0)
	Button(root,text="Save Game",command=menuc.save()).grid(row=2,column=0)
	Button(root,text="Load Game",command=menuc.load()).grid(row=3,column=0)
	Button(root,text="Options",command=menuc.options()).grid(row=4,column=0)
	Button(root,text="Quit",command=menuc.confirmquit()).grid(row=5,column=0)
