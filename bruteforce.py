#pip install requests ile indiriliyor
import requests
import time

payload={"log":"nesrin.atikturk@gmail.com" , "pwd":"Nsrnatktrk7"}
r=requests.post("https://www.siberogretmen.com/giris/?redirect_to=https%3A%2F%2Fwww.siberogretmen.com%2F", data=payload)
time.sleep(5)

#print(r.text)

if "Incorrect password" in r.text:
    print("Şifre doğru değil")

else:
    print("Şifre doğru")