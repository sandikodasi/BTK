dosya=open("sayilar.txt","w",encoding="utf-8")
for i in range(1,10000):
    dosya.write(str(i)+"\n")
print("Bilgiler başarıyla işlendi...")
dosya.close()
#pip install gTTs --> yeni kütüphane eklemek için terminale yazılır.. gTTs: kütüphane adı
