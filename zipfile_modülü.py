import zipfile
f=zipfile.ZipFile("C:/Users/ogr_8/Desktop/resim.zip")
for i in f.namelist():
    print(i)
    