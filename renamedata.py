import os

for filePath in ["raw","segment"]:

	## rename
	pathName = "./"+filePath
	allFiles = os.listdir(pathName)
	allFiles.sort()

	num = len(allFiles)

	i = 1

	for thisFile in allFiles:
		os.rename(os.path.join(pathName,thisFile),os.path.join(pathName,str(i).zfill(5)+".png"))
		# print thisFile
		i+=1

	j = 1
	for thisFile in os.listdir(pathName):
		if j % 2 == 0:
			os.remove(pathName + "./" + thisFile)
		j+=1


	print(filePath + " is Done!")