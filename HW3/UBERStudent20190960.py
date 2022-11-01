#!/usr/bin/python
import sys
import datetime
days = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
uberDic = {}
try:
	inputFile = open(sys.argv[1], "rt")
	outputFile = open(sys.argv[2], "wt")
	for line in inputFile:
		s = line.split(",")
		a = line.split(",")[1].split("/")
		day = days[datetime.date(int(a[2]), int(a[0]), int(a[1])).weekday()]
		
		keyStr = s[0] + "," + day
		if keyStr not in uberDic:
			uberDic[keyStr] = (s[2] + "," + s[3])
		else:
			v = int(uberDic[keyStr].split(",")[0]) + int(s[2])
			t = int(uberDic[keyStr].split(",")[1]) + int(s[3])
			uberDic[keyStr] = (str(v) + "," + str(t))				
	for key, value in uberDic.items():
		outputStr = key + " " + value + "\n"
		outputFile.write(outputStr)
except FileNotFoundError:
	print("FileNotFoundError")
finally:
	inputFile.close
	outputFile.close

