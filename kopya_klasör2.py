import shutil
import os

yol=os.getcwd()
for kokdizin,altdizin,dosyalar in os.walk("C:/Users/ogr_8/Desktop/fotoğraflar"):    
    for kok in kokdizin:
        for alt in altdizin:        
            for dosya in dosyalar:
                try:
                    os.mkdir(alt)
                except:
                    pass
                print(dosya)
            
        
                shutil.copy("C:/Users/ogr_8/Desktop/fotoğraflar" +"/"+ dosya, yol+"/"+ "na"),
                try:
                    shutil.copy("C:/Users/ogr_8/Desktop/fotoğraflar" +"/"+alt+"/"+ dosya, yol+"/"+alt)
                except:
                    pass
                print(kok)
                print(alt)

          
      