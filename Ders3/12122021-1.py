liste=[] #boş liste tanımlar
liste=["Elma","Armut",20] #artık listenin elemanları değişti!
sayilar=[15,19,2,3,8,25,6]
isimler=["ali","veli","ahmet","zehra","hatice"]
gunler=["Pazartesi","Salı","Çarşamba"]
print(gunler)
print("0. indeksdeki eleman:",gunler[0]) #ctrl+d çoğaltır, ctrl+y satırı siler
print(gunler[1])
print(gunler[2])
gunler.append("Perşembe") #append: yeni eleman ekler
print(gunler)
print("Eleman sayısı:",len(gunler)) #len: listenin eleman sayısını verir
gunler.pop() #hiçbirşey yazılmadıgında listenin son elemanını çıkarır
print(gunler)
gunler.pop(0)#0. indeksteki elamanı siler
print(gunler)
print(sayilar)
sayilar.sort() #varsayılan(default) olarak küçükten büyüğe doğru sıralar
print(sayilar)
sayilar.sort(reverse=True) #büyükten küçüğe doğru sıralar
print(sayilar)
isimler.sort()
print(isimler)