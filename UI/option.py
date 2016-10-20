import main

def choice(frame, choices):
	intr=0
	for i in range(0, len(choices)):
		Button(frame, text=choices[intr]).grid(row=intr, column=0)
		intr+=1
