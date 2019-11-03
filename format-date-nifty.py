import csv
import glob
from datetime import datetime

csvReader=csv.reader(open('Niftyjan7tojuly12del.csv','r'),delimiter = ',')
csvWriter=csv.writer(open('nifty-date-formatted.csv','w',newline=''),delimiter = ',')

for row in csvReader:
	data=row[0]
	df=datetime.strptime(data, '%d-%b-%y').strftime('%y%m%d')
	csvWriter.writerow(row+[df])
print("Exiting code! Bye Juhi")