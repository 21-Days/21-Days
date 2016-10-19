import main
import gui
from tkinter import *

def result(textbox,inp):
	if(inp.lower=="a"):
		textbox.insert("A")
	elif(inp.lower=="b"):
		textbox.insert("B")
	elif(inp.lower=="c"):
		textbox.insert("C")
	elif(inp.lower=="d"):
		textbox.insert("D")
	elif(inp.lower=="e"):
		textbox.insert("E")
	elif(inp.lower=="f"):
		textbox.insert("F")
	elif(inp.lower=="g"):
		textbox.insert("G")
	elif(inp.lower=="h"):
		textbox.insert("H")
	elif(inp.lower=="i"):
		textbox.insert("I")
	elif(inp.lower=="j"):
		textbox.insert("J")
	elif(inp.lower=="k"):
		textbox.insert("K")
	elif(inp.lower=="l"):
		textbox.insert("L")
	elif(inp.lower=="m"):
		textbox.insert("M")
	elif(inp.lower=="n"):
		textbox.insert("N")
	elif(inp.lower=="o"):
		textbox.insert("O")
	elif(inp.lower=="p"):
		textbox.insert("P")
	elif(inp.lower=="q"):
		textbox.insert("Q")
	elif(inp.lower=="r"):
		textbox.insert("R")
	elif(inp.lower()=="s"):
		textbox.insert("S")
	elif(inp.lower()=="t"):
		textbox.insert("T")
	elif(inp.lower()=="u"):
		textbox.insert("U")
	elif(inp.lower()=="v"):
		textbox.insert("V")
	elif(inp.lower()=="w"):
		textbox.insert("W")
	elif(inp.lower()=="x"):
		textbox.insert("X")
	elif(inp.lower()=="y"):
		textbox.insert("Y")
	elif(inp.lower()=="z"):
		textbox.insert("Z")
	elif(inp.lower()=="esc"):
		main.pause()
	elif(inp.lower()=="enter"):
		textbox.insert("/n")
		
	elif(inp=="new"):
		textbox.insert("")
	else:
def run(root):
	function.clear(root)
	Label(root, text="21 Days", font=32).grid(row=0,column=0, columnspan=2)
	out=Text(root,).grid(row=1, column=0, rowspan=3, columnspan=2)
	file=open("binds","r")
	key=file.readlines()
	tint=0
	for i in range(0,30):
		b="<"+key[tint]+">"
		out.bind(b,result(key[tint]))
		tint+=1
	main.interpreter(out,"storyline.txt")
