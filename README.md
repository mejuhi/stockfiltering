# Stockfiltering
Python files to process NSE stock price data.  
You can either use [Method 1](https://github.com/mejuhi/stockfiltering#method-1-manual-method-batch-method) (i.e. Manual Method/ Batch Method) or [Method 2](https://github.com/mejuhi/stockfiltering#method-2-automated-method) (i.e. Automated Method) for processing

## Note: Following setup is tested on windows machine. If you are using any other os(Linux or MAC os) please change the steps accordingly

## Pre-Requisite:
- Python should be installed on machine https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe   
	
## Additional Packages required (only for Automated Method)
- install requests python package
- install wtforms python package
```
pip install requests
pip install wtforms
```


## Clone the repository
```
git clone https://github.com/mejuhi/stockfiltering.git
```
	
### Method 1: Manual Method/ Batch Method

#### 1. Download all the NSE stock price zip files and place all the zip files of NSE stock price into folder Data

#### 2. Run Python file 'unzip.py'
```
python unzip.py
```
Above command will unzip all the zip files into 'Data' dir

#### 3. Create Consolidated csv file using python file 'consolidation.py'
```
python consolidation.py
```
Above command will create 'consolidated.csv' file into 'Data' dir. It will contain all the data from all the csv files in 'Data' dir 

#### 4. Filter only the EQ stocks using file 'filter-onlyEQ.py'
```
python filter-onlyEQ.py
```
Above command will create 'onlyEQ.csv' file into 'Data' dir. It will contain all the data from all the csv files in 'Data' dir 

#### 5. Format the date column using file 'format-date.py'
```
python format-date.py
``` 
Above command will create 'formated-date.csv' file into 'Data' dir. It will contain all the data from all the csv files in 'Data' dir 

#### 6. Filter the values using file 'filter-value.py'
```
python filter-value.py
```
Final Output file will be 'Data/output.csv'

#### You can now check the final processed file 'Data/output.csv' 

### Method 2: Automated Method

1. Run python file 'automated.py' and pass the argument of date for which you want processed file in "DD MMM YYYY" (01 NOV 2019)
```
python automated.py DD MMM YYYY

Example: python automated.py 01 NOV 2019
```
Above command will provide processed file as 'file/automated-output.csv' in the current working dir


### Details of the files checked in 
```
README.md:            (README) md file for documentation
file:                 (AUTOMATED METHOD) Dir which stores all the data for automated method (input as well as output)
automated.py:         (AUTOMATED METHOD) Python code for downloading and processing csv file for particular date supplied as parameter	 
Data:                 (MANUAL METHOD) Dir which stores all the data for manual method (input as well as output)
unzip.py:             (MANUAL METHOD) Python code for unziping all the zip files downloaded
consolidation.py:     (MANUAL METHOD) Python code for combining n csv files of various dates and giving out single csv file
filter-onlyEQ.py:     (MANUAL METHOD) Python code for only filtering out only Equity
format-date.py:       (MANUAL METHOD) Python code for formating date, it adds extra column with date format as 'YYMMDD' 
filter-value.py:      (MANUAL METHOD) Python code for only filtering out on value greater than 50000000
trial.py:             (REVISION) Python code used for testing out automated method
format-date-nifty.py: (REVISION) Python code to format date
download.py:          (REVISION) Python code to download csv from NSE
pre.md:               (TO BE DELETED)
```
