import os
tane=0
for kökdizin,altdizin,dosyalar in os.walk("C:/"):
    for dosyalarn in dosyalar:
        if dosyalarn.endswith(".jpg") or dosyalarn.endswith(".png"):
            print(dosyalarn)
            tane=tane+1

print(tane , "tane resim var")
       