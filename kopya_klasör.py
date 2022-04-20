import shutil
import os

#os.listdir kullanarak
 
 #for i in os.listdir("C:/Users/ogr_8/Desktop/fotoğraflar"):                      
    #shutil.copy("C:/Users/ogr_8/Desktop/fotoğraflar/" +i, "C:/Users/ogr_8/Desktop/kopyaklasör")



 #os.walk kullanarak

for kok,altdizin,dosya in os.walk("C:/Users/ogr_8/Desktop/fotoğraflar"):         
    for i in dosya:
        shutil.copy(kok +"/"+ i,"C:/Users/ogr_8/Desktop/kopyaklasör")


  
  