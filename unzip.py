import glob
import zipfile
import os 

newDir = os.getcwd()+"/Data"
os.chdir(newDir) 
cwd = os.getcwd() 
print("Current working directory is:", cwd) 
zipfiles=glob.glob('cm*.zip')
for file in zipfiles:
	print(file)
	with zipfile.ZipFile(file,'r') as zip_ref:
    		zip_ref.extractall()	
			
