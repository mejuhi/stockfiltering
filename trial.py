import requests
import sys
import glob
import csv
import os
from zipfile import ZipFile
from datetime import datetime


DATE=sys.argv[1]
MONTH=sys.argv[2]
YEAR=sys.argv[3]

url = "https://www.nseindia.com/content/historical/EQUITIES/%s/%s/cm%s%s%sbhav.csv.zip" % (YEAR, MONTH, DATE, MONTH, YEAR)
fileZip = "Zip%s%s%s.zip" % (DATE, MONTH, YEAR)
file = "cm%s%s%s.csv" % (DATE, MONTH, YEAR)

print ("INFORMATION: Connecting to " +url)
# download the file contents in binary format to healthcheck URL

print ("STAGE 1/5: Connecting to URL") 
r = requests.get(url)

# 200 means a successful request
if (r.status_code == 200):

	# open method to open a file on your system and write the contents
	print ("STAGE 2/5: Saving zip") 
	with open(fileZip, "wb") as code:
		code.write(r.content)

	#Extract all the contents of zip in new file directory (created relativve to he current dir)
	print ("STAGE 3/5: Unzip the file")	
	with ZipFile(fileZip, 'r') as zipObj:		
		zipObj.extractall('file')	
	
	#Rename extracted files

	dst = 'file/'+ file 
	for filename in os.listdir('file'): 
		src = 'file/' + filename 
		os.rename(src, dst) 
	
	print ("STAGE 4/5: Filter the data")	
	# Apply filter condition
	csvReader=csv.reader(open(dst,'r'),delimiter = ',')
	csvWriter=csv.writer(open('file/filtered.csv','w',newline=''),delimiter = ',')
	firstline = True
	for row in csvReader:
		if firstline:
			csvWriter.writerow(row)
			firstline = False
			continue
		EQCONDITIONON=row[1]
		VALUECONTIONON=row[9]
		if(EQCONDITIONON=='EQ' and float(VALUECONTIONON)>=10000000):
			csvWriter.writerow(row)

	# Format datetime
	print ("STAGE 5/5: Formating date")
	csvReader=csv.reader(open('file/filtered.csv','r'),delimiter = ',')
	csvWriter=csv.writer(open('output.csv','w',newline=''),delimiter = ',')
	firstline = True
	for row in csvReader:
		if firstline:
			csvWriter.writerow(row)
			firstline = False
			continue
		data=row[10]
		df=datetime.strptime(data, '%d-%b-%Y').strftime('%y%m%d')
		csvWriter.writerow(row+[df])
	print ("INFORMATION: All stage complete")
	print ("INFORMATION: Performing cleanup")
	os.remove(fileZip)
else:
	print ("ERROR: Something went wrong!")
	print ("Exiting Program due to Error in URL, Please try different URL")
print ("SUCCESS: Please check processed 'output.csv' file in your current directory")