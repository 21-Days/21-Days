def labels(load):
	saveInfo=[]
	if(os.path.exists("/Saves/autosave.txt")):
		file=open("/Saves/save"+intg,"r")
		save=file.readlines()
		saveInfo.add(save[1])
		file.close()
	else:
		saveInfo.add("(empty)")
	intg=1
	for i in range(0, 4):
		if(os.path.exists("/Saves/save"+intg+".txt")==True):
			file=open("/Saves/save"+intg+".txt","r")
			save=file.readlines()
			saveInfo.add(save[1])
			file.close()
		else:
			saves.add("(empty)")
	if(load==True):
		returnl.add("Auto-"+saveinfo[0])
		returnl.add("Slot1-"+saveinfo[1])
		returnl.add("Slot2-"+saveinfo[2])
		returnl.add("Slot3-"+saveinfo[3])
		returnl.add("Slot4-"+saveinfo[4])
	else
		returnl.add("Slot1-"+saveinfo[1])
		returnl.add("Slot2-"+saveinfo[2])
		returnl.add("Slot3-"+saveinfo[3])
		returnl.add("Slot4-"+saveinfo[4])
	return returnl
def load(ch):
	if(ch==0):
		file=open("autosave.txt", "r")
		main.interpreter(currentfile,"", True,section)
	elif(ch==1):
		file=open("Save1.txt", "r")
		main.interpreter(currentfile,"", True,section)
	elif(ch==2):
		file=open("Save2.txt", "r")
		main.interpreter(currentfile,"", True,section)
	elif(ch==3):
		file=open("Save3.txt", "r")
		main.interpreter(currentfile,"", True,section)
	elif(ch==4):
		file=open("Save4.txt", "r")
		main.interpreter(currentfile,"", True,section)
def save(ch):
	if(ch==0):
		file=open("autosave.txt","r")
		file.write(file+"/n")
		file.write(section)
		file.close()
	else:
	elif(ch==1):
		file=open("Save1.txt", "r")
		file.write(file+"/n")
		file.write(section)
		file.close()
	elif(ch==2):
		file=open("Save2.txt", "r")
		file.write(file+"/n")
		file.write(section)
		file.close()
	elif(ch==3):
		file=open("Save3.txt", "r")
		file.write(file+"/n")
		file.write(section)
		file.close()
	elif(ch==4):
		file=open("Save4.txt", "r")
		file.write(file+"/n")
		file.write(section)
		file.close()
