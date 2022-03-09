
f=open("sifreler2.txt", "w")

for i in range(100000,1000000):
    sayi=str(i)
    sayir=sayi[2:6]
    f.write(sayir+"\n")


