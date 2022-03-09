f=open("sayılar.txt", "a")
for i in range(0, 10000):
    sayi=str(i)
    f.write(sayi+"\n")
f.close()
