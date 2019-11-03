import csv
import glob
from datetime import datetime
import os 


newDir = os.getcwd()+"/Data"
os.chdir(newDir) 
cwd = os.getcwd() 
print("Current working directory is:", cwd) 

csvReader=csv.reader(open('consolidated.csv','r'),delimiter = ',')
csvWriter=csv.writer(open('onlyEQ.csv','w',newline=''),delimiter = ',')

for row in csvReader:
	data=row[1]
	if(data=='EQ'):
		csvWriter.writerow(row)
print("Exiting code! Bye SKG")