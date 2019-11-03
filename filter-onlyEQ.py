import csv
import glob
from datetime import datetime

csvReader=csv.reader(open('consolidated.csv','r'),delimiter = ',')
csvWriter=csv.writer(open('onlyEQ.csv','w',newline=''),delimiter = ',')

for row in csvReader:
	data=row[1]
	if(data=='EQ'):
		csvWriter.writerow(row)
print("Exiting code! Bye SKG")