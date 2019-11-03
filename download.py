import zipfile, urllib.request, shutil
url = 'https://www.nseindia.com/content/historical/EQUITIES/2019/JUL/cm09JUL2019bhav.csv.zip'
file_name = 'myzip.zip'
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall()