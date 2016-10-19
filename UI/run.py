def result(textbox,inp):
	if(inp==""):
		textbox.
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
