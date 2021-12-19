"""
Hesap Makinesi Programı
BTK - Sabah Grubu Öğrencileri İle Proje Geliştirme

"""

print("""HESAP MAKİNESİ
1- TOPLAMA
2- ÇIKARMA
3- ÇARPMA
4- BÖLME""")

secenek=input("Lütfen bir seçim yapınız:")
sayi1=int(input("1. sayıyı giriniz:"))
sayi2=int(input("2. sayıyı giriniz:"))
if secenek=="1":
    print("Sayılarınızın toplamı: ",sayi1+sayi2)
elif secenek=="2":
    print("Sayılarınızın farkı: ",sayi1-sayi2)
elif secenek=="3":
    print("Sayılarınızın çarpımı: ",sayi1*sayi2)
elif secenek=="4":
    print("Sayılarınızın bölümü: ",sayi1/sayi2)
else:
    print("Lütfen 1-4 arası bir seçim yapınız!")


