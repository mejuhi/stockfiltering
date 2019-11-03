import csv
import glob
from datetime import datetime
import os 


newDir = os.getcwd()+"/Data"
os.chdir(newDir) 
cwd = os.getcwd() 
print("Current working directory is:", cwd) 

print("Starting Execution!")
csvReader=csv.reader(open('onlyEQ.csv','r'),delimiter = ',')
csvWriter=csv.writer(open('formated-date.csv','w',newline=''),delimiter = ',')

for row in csvReader:
	data=row[10]
	df=datetime.strptime(data, '%d-%b-%Y').strftime('%y%m%d')
	csvWriter.writerow(row+[df])
	
print("Exiting code! Bye SKG")