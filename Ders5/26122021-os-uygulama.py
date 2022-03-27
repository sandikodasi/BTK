#kendisine verilen sayı kadar bulunduğu yere klasor olusturan fonksiyonu yazınız

















import os
def klasor_olustur(x):
    for i in range(x):
        os.mkdir("Deneme1/"+ "virüs"+str(i+1))
sayi=int(input("Kaç tane klasor oluşturulsun"))
klasor_olustur(sayi)