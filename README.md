# Stockfiltering
Simple python files to filter NSE stock price data

## Note: Following commands and setup is tested on windows machine. If you are using Linux or any other os please change the steps accordingly

## Pre-Requisite:
- Python should be installed on machine https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe   
	
## Additional Packages required for Automated Method
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


