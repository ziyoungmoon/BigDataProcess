#!/usr/bin/python
import sys
from datetime import datetime, date

def what_day_is_it(date):
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        day = date.weekday()
        return days[day]

read = sys.argv[1]
write = sys.argv[2]
uberDic = {}

fp = open(read, "rt")
for line in fp :
    s_arr = line.split(',')
    date_str = s_arr[1].split('/')
    date = what_day_is_it(int(date_str[2], int(date_str[0]), int(date_str[1])))

    key = s_arr[0] + "," + date
	if key not in uberDic:
	    uberDic[key] = (s_arr[2] + "," + s_arr[3])
	else:
		v = int(uberDic[key].split(",")[0]) + int(s_arr[2])
		t = int(uberDic[key].split(",")[1]) + int(s_arr[3])
		uberDic[key] = (s_arr(v) + "," + s_arr(t))				
fp.close()

f = open(write, 'wt')
for key, count in uberDic.items():
    f.write(key[0] + "," + key[1])
    f.write(" %d,%d\n" % (count[0], count[1]))
f.close()
