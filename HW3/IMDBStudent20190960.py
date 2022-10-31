#!user/bin/python3
import sys

read = sys.argv[1]
write = sys.argv[2]
list = []
f = open(read, "rt")
for line in f:
	m = line.split('::')
	genre = m[2].split('\n')
	g = genre[0].split('|')
	for g1 in g:
		list.append(g1)
dict = {}
for i in list:
	if dict.get(i):
		dict[i] += 1
	else:
		dict[i] = 1
w = open(write, "wt")
for key, value in dict.items():
	w.write(key + " " + str(value) + "\n")
w.close()
f.close()

	
