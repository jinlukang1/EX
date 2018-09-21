# -*- coding: utf-8 -*-  
# 重命名图片文件，并把图片拼接为视频
import os,math


# now="morning" # 710
now="noon"    # 1150
# now="evening"   # 1750
# now="night"	# 2200

# weather = "sunny"       # default : Cloud Density 1.25 ;  
# weather = "lightFog"
# weather = "heavyFog"	  # Cloud Density 3 ; 
# weather = "lightRain"   # Cloud Density 2 ; 
# weather = "heavyRain"	  # Cloud Density 3 ; 	
weather = "lightSnow"
# weather = "heavySnow"	  # Cloud Density 3 ; 	
# weather = "blizzard"
# weather = "hail"


# filePath = "raw"
# filePath = "segment"
# filePath = "depth"

for filePath in ["raw","segment","depth"]:

	## rename
	pathName = "./"+filePath
	allFiles = os.listdir(pathName)
	allFiles.sort()

	num = len(allFiles)
	# print num
	start = (int)(allFiles[0][8:18]);
	# print start
	end = (int)(allFiles[num-1][8:18]);
	# print end
	fps = math.ceil(1.0*num/(end-start))
	print 'fps:',fps
	# fps = 4

	# img_0_0_1527049076---349293800
	# we can see how many files there are in one second shown by 076
	# it's obvious that the bigger or more the file, the lower the fps. 900*600->2.x , 500*400->4.x 
	# 如果把主屏幕关掉"ViewMode": "NoDisplay",，fps更高，但是前面几张图要忽略，后面能稳定在6.x, "RecordInterval": 0.05 也很重要

	i = 1
	for thisFile in allFiles:
		os.rename(os.path.join(pathName,thisFile),os.path.join(pathName,str(i).zfill(5)+".png"))
		# print thisFile
		i+=1

	## make vedio from images
	stat = os.popen("ffmpeg -y -r "+ str(fps) + " -i " + filePath + "/%05d.png " + weather + "_" + now + "_" + filePath +".mp4")
	print stat.read()
	print weather + "_" + now,filePath+" is done\r\n"

	# status, output = commands.getstatusoutput("ffmpeg  -y -r 10 -i "+filePath+"/%05d.png "+filePath+"output.mp4")
	# print stat.output