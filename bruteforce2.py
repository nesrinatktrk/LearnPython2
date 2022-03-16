import requests
import time

payload={"log":"nesrin" , "pwd":"44"}
r=requests.post("http://bmi.ym.edu.tw/wp/wp-login.php", data=payload)
time.sleep(5)

#print(r.text)

if "Incorrect password" in r.text:
    print("Şifre doğru değil")

else:
    print("Şifre doğru")