#For UE4
import time
import random

class ModifiedFile:

	def __init__(self, FileName):
		self.FileName = FileName

	def ReadCon(self):#读出文件内容
		fileObject = open(self.FileName, "r")
		num = fileObject.readline()
#		print(num)
		fileObject.close()
		return num

	def WriteCon(self, NewNum):#对文件进行写入操作
		fileObject = open(self.FileName, "w")
		fileObject.write(NewNum)
		fileObject.close()

def Num_random(FileToSave, Num = [], Num_range = []):#随机并进行随机数据的储存
	for i in range(7):
		Num[i].WriteCon(str(random.randint(0, Num_range[i])))
	for j in range(7):
		FileToSave.write(Num[j].ReadCon())
		FileToSave.write(" ")

RecordFile = open('G:/Record.txt', 'a')

Num = []
Num.append(ModifiedFile("G:/Num_1.txt"))
Num.append(ModifiedFile("G:/Num_2.txt"))
Num.append(ModifiedFile("G:/Num_3.txt"))
Num.append(ModifiedFile("G:/Num_4.txt"))
Num.append(ModifiedFile("G:/Num_5.txt"))
Num.append(ModifiedFile("G:/Num_6.txt"))
Num.append(ModifiedFile("G:/Num_7.txt"))


Num_range = [10, 10, 10, 10, 10, 10, 10]#设定每个字符随机范围

for j in range(5):#设定产生数据次数
	Num_random(RecordFile, Num, Num_range)
	time.sleep(1)#修改间隔时间
	RecordFile.write('\n')

