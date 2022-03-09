#w=write --var olan dosyanın yada kendi oluşturduğu dosyanın içindekileri silip yeni yazılar ekletir.
#a=append --var olan dosyadaki yada kendi oluşturduğu dosyadaki yazılara yenilerini eklemeni sağlar.
#r=read --var olan dosyayı okutur.
#string olmayan bir yazı yazılamıyor!

f=open("şifreler.txt", "w")
f.write("deneme")
f.close()
f=open("sayi.txt","a")
f.write("hey")
f.close()