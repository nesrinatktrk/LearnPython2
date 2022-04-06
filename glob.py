#a ile başlayan dosyanın yanında rakam oldupğunu biliyoruz a ile başlayanve yanında rakam olan dosyaları bul
import glob
dosya=glob.glob("C:/Users/ogr_8/Desktop/a*.txt")
print(dosya)


for i in glob.glob("C:/Users/ogr_8/Desktop/a*.txt"):
    print(i)