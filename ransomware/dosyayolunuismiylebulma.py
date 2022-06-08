import os
istenilen=input("Dosya: ")
adres=os.path.join(os.path.join(os.environ['USERPROFILE']),"Desktop")
adresno=adres+"/"+istenilen
adresn=adresno.replace(os.sep, '/')
for kökdizin,altdizin,dosyalar in os.walk(adresn):
    for yol in kökdizin:
        print(yol)
        

#içinde ismi içeren başka sonuç bulunursa hepsini kullanıcıya sor