#Kullanıcıdan verilerek alarak dikdortgenin çevresini hesaplayınız
print("DİKDÖRTGEN HESAPLAMALARI")
secim=input("Hesaplama türünü seçiniz (çevre/alan):").lower()

if secim=="çevre":
    kisa_kenar=int(input("Kısa kenarı giriniz:"))
    uzun_kenar=int(input("Uzun kenarı giriniz:"))
    print("Dikdörtgenin çevresi:",(kisa_kenar+uzun_kenar)*2)
elif secim=="alan":
    kisa_kenar=int(input("Kısa kenarı giriniz:"))
    uzun_kenar=int(input("Uzun kenarı giriniz:"))
    print("Dikdörtgenin alanı:",kisa_kenar*uzun_kenar)
else:
    print("Lütfen çevre ya da alan yazınız!")