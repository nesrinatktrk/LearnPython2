from cryptography.fernet import Fernet
def keyUret():
    key=Fernet.generate_key()  #Key üret
    with open("key.txt","wb") as keyDosyasi:  #Keyi unutmamak için dosyaya kaydet
        keyDosyasi.write(key)

def dosyaAc(dosya):
    with open(dosya,"rb") as dosyam:
        return dosyam.read()  #Keyi daha sonra kullanmak için keyi oku

def sifrele(dosyalar,key,içerik):
    f=Fernet(key)
    şifreliiçerik=f.encrypt(içerik)
    with open(dosyalar,"wb") as dosyalar:
        dosyalar.write(şifreliiçerik)


key = dosyaAc("key.txt") 


içerik1=dosyaAc("metin1.txt")
içerik2=dosyaAc("metin2.txt")
içerik3=dosyaAc("metin3.txt")
print(key)
print(içerik1)
sifrele("metin1.txt",key,içerik1)

keyUret()
    
f=Fernet(key)
şifreliiçerik1=f.encrypt(içerik1)
with open("metin1.txt", "wb") as dosyalar:
    dosyalar.write(şifreliiçerik1)

şifreliiçerik2=f.encrypt(içerik2)
with open("metin2.txt", "wb") as dosyalar:
    dosyalar.write(şifreliiçerik2)

şifreliiçerik3=f.encrypt(içerik3)
with open("metin2.txt", "wb") as dosyalar:
    dosyalar.write(şifreliiçerik3)

