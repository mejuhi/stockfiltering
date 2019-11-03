import csv
import glob
from datetime import datetime

csvReader=csv.reader(open('formated-date.csv','r'),delimiter = ',')
csvWriter=csv.writer(open('output.csv','w',newline=''),delimiter = ',')

for row in csvReader:
	data=row[9]
	#print(data)
	if(float(data)>=50000000):
		csvWriter.writerow(row)
	#print(df)
#dt = datetime.datetime.strptime('04-May-2018',"%d-%b-%y")
#print(dt)
print("Exiting code! Bye SKG")