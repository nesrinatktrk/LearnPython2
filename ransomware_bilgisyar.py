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

for kok,altdizin,dosya in os.walk("C:/Users/Nesrin/Desktop/bilgisayar"):         
    for i in dosya:
        def sifrele(dosyalar,key):
            içerik=dosyaAc(dosyalar)
            f=Fernet(key)
            şifreliiçerik=f.encrypt(içerik)
            with open(dosyalar,"wb") as dosyalar:
                dosyalar.write(şifreliiçerik)

        sifrele(i,key)


    