def saveload(load, file, section, auto):
	if(auto==True):
		print("AutoSaving...")
		file=open()
		file.write(file+"/n")
		file.write(section)
		file.close()
		print("AutoSave Done!")
	else:
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
			intg+=1
		if(load==True):
			SaveFileChoices="""
Options:
	0. AutoSave-"""+saveinfo[0]+"""
	1. Save1-"""+saveInfo[1]+"""
	2. Save2-"""+saveInfo[2]+"""
	3. Save3-"""+saveInfo[3]+"""
	4. Save4-"""+saveInfo[4]+"""
	5. Exit"""
		else:
			SaveFileChoices="""
Options:
	1. Save1-"""+saveInfo[1]+"""
	2. Save2-"""+saveInfo[2]+"""
	3. Save3-"""+saveInfo[3]+"""
	4. Save4-"""+saveInfo[4]+"""
	5. Exit"""
		ch=input(SaveFileChoices)
		if(load==True)
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
			else:
				print("Exiting Loadgame Menu...")
		else:
			if(ch==1):
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
			else:
				print("Exiting Savegame Menu...")
