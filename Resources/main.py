import time

global currentSection
global file
global exitcode
def interpreter(fille, split, loadgame, section):
	if(split!=""):
		if(split.upper()=="WAY0" or split.upper()=="WAY 0" or split.upper()=="0")
			file=open("/Resources/"+fille+"-0.txt","r")
		elif(split.upper()=="WAY1" or split.upper()=="WAY 1" or split.upper()=="1")
			file=open("/Resources/"+fille+"-1.txt","r")
		else:
			input("LOAD_ERROR, press any key to exit.")
			exit()
	elif(loadgame==True):
		file=open("/Resources/"+fille,"r")
	else:
		file=open(fille, 'r')
	temp=open("temp.txt", 'wb')
	story=file.readlines()
	int=0
	line=story[int]
	while(exitcode not 0):
		if("INPUT" in line):
			foo=line.upper().replace("INPUT ", "")
			lsts=foo.split(',', 1)
			while(var==""):
				var=input(lsts[0])
			temp.seek(0, 2)
			temp.write(lsts[1]+"="+var)
		elif("SECTION:" in line):
			cu=line.replace("SECTION: ", "")
			cus=cu.replace(".", " ")
			currS=cus.split(' ', 1)
			chapter=currS[0]
			scene=currS[1]
			option=currS[2]
			finncS=str("CHAPTER "+chapter+", SCENE "+scene+", OPTION "+option)
			print(finncS)
			currentSection=finncS
			time.wait(3)
		elif("+ " and " +" in line):
			j=line.split(' + ', 1)
			j.pop(0)
			j.pop(1)
			jkl=j[0]
			jklm=temp.readline()
			while(jkl not in jklm)
				jklm=temp.readline()
				if(jklm="")
					input("ERROR! FILE COULD NOT BE READ!")
					exitcode=1
			lolls=jklm.replace(jkl+"=", "")
			loolls=line.replace("+ "+jkl+" +", lolls)
			input(loolls)
		elif("SPLIT " in line):
			jklomp=line.replace("SPLIT ", "")
			jollo=jklomp.split(',' ,1)
			jol=jollo[0].upper()
			llo=jollo[1].upper()
			interpreter(jol, llo)
		elif("SKIP" in line):
			lomlom=str(line.replace("SKIP ", ""))
			ple= int(lomlom)
			file.seek(ple, 0)
		elif("python" in line.lower()):
			kmslol=line.lower().replace("python(","")
			lolsmk=kmslol.replace(")","")
			filelele=open("run.py", "wb")
			k="""
def run():
	"""+lolsmk+"""
#THIS IS ONLY TEMPORARY..."""
			filelele.write(k)
			if(args):
				import run
				run.run()
			filelele.close()
		elif("RND" in line):
			arggggggghhhs=line.replace(" ","").replace("RND(", "").replace(")","").split(',', 1)
			random.randint(arggggggghhhs[0], arggggggghhhs[1])
		elif("" in line):
		elif("SAVE" in line.upper()):
			saveload.save(0)
			print("GAME AUTOSAVED.")
		elif(line=="FINAL"):
			exitcode=0
			break
		elif(line=="*START*"):
			active=True
		elif(line=="*END*"):
			out=
		else:
			inesa=input(line)
			if("exit" in inesa.lower()):
				exitcode
			elif("save"):
				saveload.save(input("Which spot would you like to save in? (Type in the number)\n"+saveload.getinfo("all")))
		int+=1
	temp.close()
	file.close()
	return exitcode
