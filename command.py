# coding:utf-8

import time
import random

'''
字符一对应范围（Num_1.txt-Num_7.txt）
1-京, 2-津, 3-冀, 4-晋, 5-蒙, 6-辽, 7-吉, 8-黑, 9-沪, 10-苏, 11-浙, 12-皖, 
13-闽, 14-赣, 15-鲁, 16-豫, 17-鄂, 18-湘, 19-粤, 20-桂, 21-琼, 22渝, 23-川, 
24-贵, 25-云, 26-藏, 27-陕, 28-甘, 29-青, 30-宁, 31-新。
字符二对应范围
1-A, 2-B, 3-C, 4-D, 5-E, 6-F, 7-G, 8-H, 9-I, 10-J, 11-K, 12-L, 13-M, 14-N, 
15-O, 16-P, 17-Q, 18-R, 19-S, 20-T, 21-U, 22-V, 23-W, 24-X, 25-Y, 26-Z.
字符三到字符七对应范围
1-A, 2-B, 3-C, 4-D, 5-E, 6-F, 7-G, 8-H, 9-J, 10-K, 11-L, 12-M, 13-N, 
14-P, 15-Q, 16-R, 17-S, 18-T, 19-U, 20-V, 21-W, 22-X, 23-Y, 24-Z, 
25-1, 26-2, 27-3, 28-4, 29-5, 30-6, 31-7, 32-8, 33-9, 34-0.
天气对应范围（Weather.txt)
1-冰雹, 2-暴雪, 3-大雪, 4-小雪, 5-大雨, 6-小雨, 7-大雾, 8-小雾。
汽车类型变化范围（Car_type.txt）
1-SUV, 2-黑色小轿车, 3-红色小轿车, 4-出租车。
摄像机角度距离变化范围（Camera_set.txt）
1-手持, 2-卡口, 3-车载, 4-安防监控, 5-无人机俯视。
'''

NUM_list = [["京", "津", "冀", "晋", "蒙", "辽", "吉", "黑", "沪", "苏", "浙", "皖", 
"闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "渝", "川", "贵", "云", 
"藏", "陕", "甘", "青", "宁", "新"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", 
"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", 
"5", "6", "7", "8", "9", "0"], ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", 
"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", 
"5", "6", "7", "8", "9", "0"], ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", 
"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", 
"5", "6", "7", "8", "9", "0"], ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", 
"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", 
"5", "6", "7", "8", "9", "0"], ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", 
"P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", 
"5", "6", "7", "8", "9", "0"], ["冰雹", "暴雪", "大雪", "小雪", "大雨", "小雨", "大雾", "小雾"], 
["SUV", "黑色小轿车", "红色小轿车", "出租车"], ["手持", "卡口", "车载", "安防监控", "无人机俯视"]]

txtPath = "G:/txtrec/"

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
	for i in range(10):
		Num[i].WriteCon(str(random.randint(0, Num_range[i]-1)))

	for j in range(10):
		FileToSave.write(NUM_list[j][int(Num[j].ReadCon())])
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
Num.append(ModifiedFile("G:/Weather.txt"))
Num.append(ModifiedFile("G:/Car_type.txt"))
Num.append(ModifiedFile("G:/Camera_set.txt"))


Num_range = [31, 26, 34, 34, 34, 34, 34, 8, 4, 5]#设定每个字符随机范围

i = 1
for j in range(10000):#设定产生数据次数
	Num_random(RecordFile, Num, Num_range)
	
	txtFile = open(txtPath + str(i).zfill(5) + ".txt","w")

	for k in range(10):
		txtFile.write(Num[k].ReadCon())
		txtFile.write('\n')

	time.sleep(1)#修改间隔时间
	RecordFile.write('\n')

	i+=1

