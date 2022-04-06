#os.walk ve glob kütüphanelerini birleştirmeyi dene
import os
import glob


for kokklasor,altklosor,dosyalar in os.walk("C:/"):
    print(kokklasor)
    #globlu=glob.glob(kokklasor+"a??.txt")
    #for dosya in globlu:
     #   print(dosya)