#Kullanıcının istediği bütün dosyalar şifrelenecek. Uygulama girişinde 1-dosya şifrele 2-dosya çözme 3-çıkış 4-hakkında
import os
from cryptography.fernet import Fernet

while True:

    print(""" Uygulamaya hoş geldiniz...
    1-Dosyalarınızı şifrelemek
    2-Dosyalarınızdaki şifreyi kaldırmak
    3-Çıkış
    4-Hakkında""")
    başla=input("seçim...")


    def keyUret():
        key=Fernet.generate_key()  #Key üret
        with open("key.txt","wb") as keyDosyasi:  #Keyi unutmamak için dosyaya kaydet
            keyDosyasi.write(key)
    #keyUret()

    def dosyaAc(dosya):
        with open(dosya,"rb") as dosyam:
            return dosyam.read()  #Keyi daha sonra kullanmak için keyi oku

    key = dosyaAc("key.txt") 

    if başla == "1":
        istenilen=input("Şifrelemek istediğiniz dosya: ")
        def sifrele(dosya,key):
            içerik=dosyaAc(dosya)
            f=Fernet(key)
            şifreliiçerik=f.encrypt(içerik)
            with open(dosya,"wb") as dosyalar:
                dosyalar.write(şifreliiçerik)

        sifrele(istenilen,key)

    if başla == "2":
        istenilen=input("Şifresini kaldırmak istediğiniz dosya: ")
        def sifreCoz(dosya,key):
            içerik=dosyaAc(dosya)
            f=Fernet(key)
            şifreliiçerik=f.decrypt(içerik)
            with open(dosya,"wb") as dosyalar:
                dosyalar.write(şifreliiçerik)

        sifreCoz(istenilen,key)

    if başla=="3":
        print("Uygulamayı kullandığınız için teşekkürler...")
        break

   
