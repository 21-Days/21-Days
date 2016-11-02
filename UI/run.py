import main
import gui
from tkinter import *

global linecontents

def result(textbox,inp):
	linecontents=[]
	if(inp.lower=="a"):
		textbox.insert("A")
		linecontents.add("A")
	elif(inp.lower=="b"):
		textbox.insert("B")
		linecontents.add("B")
	elif(inp.lower=="c"):
		textbox.insert("C")
		linecontents.add("C")
	elif(inp.lower=="d"):
		textbox.insert("D")
		linecontents.add("D")
	elif(inp.lower=="e"):
		textbox.insert("E")
		linecontents.add("E")
	elif(inp.lower=="f"):
		textbox.insert("F")
		linecontents.add("F")
	elif(inp.lower=="g"):
		textbox.insert("G")
		linecontents.add("G")
	elif(inp.lower=="h"):
		textbox.insert("H")
		linecontents.add("H")
	elif(inp.lower=="i"):
		textbox.insert("I")
		linecontents.add("I")
	elif(inp.lower=="j"):
		textbox.insert("J")
		linecontents.add("J")
	elif(inp.lower=="k"):
		textbox.insert("K")
		linecontents.add("K")
	elif(inp.lower=="l"):
		textbox.insert("L")
		linecontents.add("L")
	elif(inp.lower=="m"):
		textbox.insert("M")
		linecontents.add("M")
	elif(inp.lower=="n"):
		textbox.insert("N")
		linecontents.add("N")
	elif(inp.lower=="o"):
		textbox.insert("O")
		linecontents.add("O")
	elif(inp.lower=="p"):
		textbox.insert("P")
		linecontents.add("P")
	elif(inp.lower=="q"):
		textbox.insert("Q")
		linecontents.add("Q")
	elif(inp.lower=="r"):
		textbox.insert("R")
		linecontents.add("R")
	elif(inp.lower()=="s"):
		textbox.insert("S")
		linecontents.add("S")
	elif(inp.lower()=="t"):
		textbox.insert("T")
		linecontents.add("T")
	elif(inp.lower()=="u"):
		textbox.insert("U")
		linecontents.add("U")
	elif(inp.lower()=="v"):
		textbox.insert("V")
		linecontents.add("V")
	elif(inp.lower()=="w"):
		textbox.insert("W")
		linecontents.add("W")
	elif(inp.lower()=="x"):
		textbox.insert("X")
		linecontents.add("X")
	elif(inp.lower()=="y"):
		textbox.insert("Y")
		linecontents.add("Y")
	elif(inp.lower()=="z"):
		textbox.insert("Z")
		linecontents.add("Z")
	elif(inp.lower()=="esc"):
		main.pause()
	elif(inp.lower()=="enter"):
		textbox.insert("/n")
		main.return(linecontents)
		for i in range(0, len(linecontents)):
			linecontents.pop(0)
	elif(inp=="new"):
		textbox.insert("/n")
	else:
def run(root):
	function.clear(root)
	Label(root, text="21 Days", font=32).grid(row=0,column=1, columnspan=2)
	out=Text(root).grid(row=1, column=0, rowspan=3, columnspan=3)
	file=open("binds","r")
	key=file.readlines()
	tint=0
	for i in range(0,30):
		b="<"+key[tint]+">"
		out.bind(b,result(key[tint]))
		tint+=1
	main.interpreter(out,"storyline.txt")
	choice=Frame(root).grid(row=1, column=4)
