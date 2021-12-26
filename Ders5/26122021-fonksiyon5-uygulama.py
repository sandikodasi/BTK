#Kullanıcıdan verileri alarak dikdortgen  çevresini ve alanını hesaplayınız
# hesaplamaları fonksiyon ile yapınız!

#Kullanıcıdan verilerek alarak dikdortgenin çevresini hesaplayınız

def cevre(kisa,uzun):
    print("Dikdörtgenin çevresi:",(kisa+uzun)*2)
def alan(kisa,uzun):
    print("Dikdörtgenin alanı:",kisa*uzun)
print("DİKDÖRTGEN HESAPLAMALARI")
secim=input("Hesaplama türünü seçiniz (çevre/alan):").lower()
kisa_kenar=int(input("Kısa kenarı giriniz:"))
uzun_kenar=int(input("Uzun kenarı giriniz:"))

if secim=="çevre":
    cevre(kisa_kenar,uzun_kenar)
elif secim=="alan":
    alan(kisa_kenar,uzun_kenar)
else:
    print("Lütfen çevre ya da alan yazınız!")