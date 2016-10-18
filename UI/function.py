from tkinter import *

def clear(root):
	for widget in root.winfo_children():
		widget.destroy()
