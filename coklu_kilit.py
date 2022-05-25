from cryptography.fernet import Fernet
def keyUret():
    key=Fernet.generate_key()  #Key üret
    with open("key.txt","wb") as keyDosyasi:  #Keyi unutmamak için dosyaya kaydet
        keyDosyasi.write(key)

def dosyaAc(dosya):
    with open(dosya,"rb") as dosyam:
        return dosyam.read()  #Keyi daha sonra kullanmak için keyi oku

key = dosyaAc("key.txt") 

def sifrele(dosya,key):
    içerik=dosyaAc(dosya)
    f=Fernet(key)
    şifreliiçerik=f.encrypt(içerik)
    with open(dosya,"wb") as dosyalar:
        dosyalar.write(şifreliiçerik)



sifrele("metin1.txt",key)
sifrele("metin2.txt",key)
sifrele("metin3.txt",key)

