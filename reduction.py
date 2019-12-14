import xlrd
import csv
import os
import pandas as pd
import sys

#Notify user about the dates entered
print("--------------STAGE 1/5--------------")
removeDates = sys.argv[1].split(',')
print("NOTE: Program will filter out following dates: ")
print(*removeDates, sep = "\n")

#Set current working directory
print("--------------STAGE 2/5--------------")
newDir = os.getcwd()+"/Reduce"
os.chdir(newDir) 
cwd = os.getcwd() 
print("Current working directory is:", cwd) 
print("Starting Execution!")

#Fetch excel input file, and output csv file
print("--------------STAGE 3/5--------------")
inputFileName = "Consol_Data(nse)Review.xlsx"
outputCSVName = "Consol_Data(nse)Review_csv.csv"
data_xls = pd.read_excel(inputFileName, 'Sheet1', index_col=None)
data_xls.to_csv(outputCSVName, encoding='utf-8')
print("File converted from .xlsx to .csv")



#Read and write output file
print("--------------STAGE 4/5--------------")
csvReader=csv.reader(open(outputCSVName,'r'),delimiter = ',')
csvWriter=csv.writer(open('reduced.csv','w',newline=''),delimiter = ',')
print("Reading newly created csv file and creating output csv file")

#Filter based on array of date received as input from command line
print("--------------STAGE 5/5--------------")
rownum = 0
for row in csvReader:
			data=row[3]
		#for date in removeDates:
			removeData = str(data).split('.')
			dateIncsv =	removeData[0]		
			#compareDate = date.strip()
			if(dateIncsv in removeDates):
				#print("Removing entry")
			else:
				csvWriter.writerow(row)

#Notify user about output file 
print("MAKE NOTE:")
print("Processed file saved in location: " + cwd )
print("Name of file saved is: reduced.csv")
print("Exiting code!")