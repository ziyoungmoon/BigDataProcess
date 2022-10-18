#!usr/bin/python3
import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['Sheet1']

list_grade = []
list_total = []

row_id = 1
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
		list_grade.append([row_id, sum_v])
	row_id += 1
	
list_total = sorted(list_grade, key = lambda x:x[1])
a = int(len(list_total) * 0.3)
ap = int(a * 0.5)
b = int((len(list_total) * 0.7) - a)
bp = int(b * 0.5)
c = int(len(list_total) - a -b)
cp = int(c * 0.5)



for i in range(len(list_total)):
	if i <= ap:
		ws.cell(row = list_total[i][0], column = 8).value = 'A+'
	elif i <= a:
		ws.cell(row = list_total[i][0], column = 8).value = 'A0'
	elif i <= bp:
		ws.cell(row = list_total[i][0], column = 8).value = 'B+'
	elif i <= b:
		ws.cell(row = list_total[i][0], column = 8).value = 'B0'
	elif i <= cp:
		ws.cell(row = list_total[i][0], column = 8).value = 'C+'
	elif i <= c:
		ws.cell(row = list_total[i][0], column = 8).value = 'C0'
	i += 1
wb.save("student.xlsx")
wb.close()
		
		
			
