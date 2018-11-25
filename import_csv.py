import csv

#exampleFile = open('working_files/example.csv')
#exampleReader = csv.reader(exampleFile)

#exampleData = list(exampleReader)
#print(exampleData[0][0]) 

#for row in exampleReader:
	#print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


###
opener1 = open('working_files/example1.csv')
reader1 = csv.reader(opener1, delimiter=',', qoutechar='"')
row1 = reader1.next()

opener2 = open.('working_files/example2.csv')
reader2 = csv.reader(opener2, delimiter=',', qoutechar='"')
row2 = reader2.next()

for row1 in reader1:
	for row2 in reader2:
		if (row1[0][1] == row2[0][1])

for row1, row2 in enumerate([row1, row2]):
	if row[0][1] != row2[0][1]
		row1[0][1] = row2[0][1]

csvWriter1 = csv.writer(row1)
for row in csvRows:
	csv.Writer.writerow(row2)
row1.close()