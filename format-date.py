import csv
import glob
from datetime import datetime

print("Starting Execution!")
csvReader=csv.reader(open('onlyEQ.csv','r'),delimiter = ',')
csvWriter=csv.writer(open('formated-date.csv','w',newline=''),delimiter = ',')

for row in csvReader:
	data=row[10]
	df=datetime.strptime(data, '%d-%b-%Y').strftime('%y%m%d')
	csvWriter.writerow(row+[df])
	
print("Exiting code! Bye Skg Gupta")