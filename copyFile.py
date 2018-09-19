# -*- coding: utf-8 -*-  
# 把文件从airsim中拷贝到ffmpeg文件夹中
import os,shutil
import time

airsimPath = "D:/Documents/AirSim/"
# datetime = "2018-05-23-16-24-44"
allFiles = os.listdir(airsimPath)
allFiles.sort()
# print allFiles[len(allFiles)-3]#有两个setting.json 所以是倒数第3个
datetime = allFiles[len(allFiles)-3]
# time.sleep(100)
realPath = airsimPath + datetime + "/images/"
print realPath

targetP = "D:/workspace/Unreal Projects/AirSim/PythonClient/temp/FFmpeg/bin/"
targetD = targetP + "depth/"
targetS = targetP + "segment/"
targetR = targetP +"raw/"

try:
	shutil.rmtree(targetD)
	shutil.rmtree(targetS)
	shutil.rmtree(targetR)
except: 
	print "Remove Error"
os.mkdir(targetD)
os.mkdir(targetS)
os.mkdir(targetR)
print "successfully make dir"


alllist = os.listdir(realPath)
for thisFile in alllist:
	if "_0_0" in thisFile:
		shutil.copyfile(realPath+thisFile,targetR+thisFile)
	elif "_0_3" in thisFile:
		shutil.copyfile(realPath+thisFile,targetD+thisFile)
	elif "_0_5" in thisFile:
		shutil.copyfile(realPath+thisFile,targetS+thisFile)

print "successfully moved"
		
