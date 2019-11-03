import glob
import zipfile

zipfiles=glob.glob('cm*.zip')
for file in zipfiles:
	print(file)
	with zipfile.ZipFile(file,'r') as zip_ref:
    		zip_ref.extractall()