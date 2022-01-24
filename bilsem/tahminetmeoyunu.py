import random
tahmin=random.randint(0,50)
while True:
    sayi=int(input("Tahmininizi giriniz:"))
    if sayi==tahmin:
        print("Başardınız!")
        break
    if sayi > tahmin:
        print("sayınızı daha küçük bir sayı seçin")
    if sayi < tahmin:
        print("Sayınızı daha büyük bir sayı seçin")
