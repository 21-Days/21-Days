from tkinter import *
import menuc
import main
import function
from lib import webbrowser

def main(root):
	function.clear()
	file=open("menutitles.txt","r")
	sub=file.readlines()
	Label(root,text="21 Days",font=32).grid(0,0)
	textn=random.randint(0,15)
	txt=sub[textn]
	if("EASTER" in txt):
		Button(root,text="Easter Egg Button",command=).grid(row=3,column=0)
	else:
		Button(root,text="Easter Egg Button",command=).grid(row=3,column=0)
	Button(root,text=txt,font=12,command=textn+=1).grid(row=1,column=0)
	Button(root,text="Play!",command=GUI_main.run(root)).grid(row=2,column=0)
	Button(root,text="Load Save",command=menuc.load(root)).grid(row=4,column=0)
	Button(root,text="Options",command=menuc.options(root)).grid(row=5,column=0)
	Button(root,text="Credits",command=menuc.credits(root)).grid(row=6,column=0)
	Button(root,text="Visit us on Github!",command=webbrowser.open("http://github.com/RGTN",new=1,autoraise=True)).grid(row=7,column=0)
	Button(root,text="Quit",command=main.exit()).grid(row=8,column=0)
	root.mainloop()
def ingame(root):
	function.clear(root)
	file=open("menutitles.txt","r")
	title=file.readlines()
	Label(root,text=title[random.randint(0,15)]).grid(row=0,column=0)
	Button(root,text="Resume Game", command=main.resume(root)).grid(row=1,column=0)
	Button(root,text="Save Game",command=menuc.save(root)).grid(row=2,column=0)
	Button(root,text="Load Game",command=menuc.load(root)).grid(row=3,column=0)
	Button(root,text="Options",command=menuc.options(root)).grid(row=4,column=0)
	Button(root,text="Quit",command=menuc.confirmquit(root)).grid(row=5,column=0)
	root.mainloop()
def exit()
	exit()
