import glob
import csv
import os 


newDir = os.getcwd()+"/Data"
os.chdir(newDir) 
cwd = os.getcwd() 
print("Current working directory is:", cwd) 
csvfiles=glob.glob('cm*.csv')
wf=csv.writer(open('consolidated.csv','w',newline=''),delimiter = ',')
for files in csvfiles:
	print (files)
	rd=csv.reader(open(files,'r'),delimiter = ',')
	next(rd)
	for row in rd:
		#print row
		wf.writerow(row)
