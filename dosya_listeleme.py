#masaüstündeki dosyaları listele
import os
desktop=os.chdir("C:/Users/ogr_8/Desktop")
for i in os.listdir(desktop):
    print(i)
