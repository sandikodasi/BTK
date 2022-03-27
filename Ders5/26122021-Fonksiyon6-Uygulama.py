#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek
#sonucunda True ya da False gönderen fonksiyonun python kodu
#kullanıcıadı: admin, şifre:123456 olmalı


def kontrol(kullanici,sifre):
    if kullanici=="admin" and sifre=="123456":
        return True
    else:
        return False
kullanici=input("Kullanıcı adınız:")
sifre=input("Şifreniz:")
sonuc=kontrol(kullanici,sifre)
if sonuc==True:
    print("doğru giriş")
else:
    print("Kullanıcı adı veya sifre hatalı")







def kontrolet(kullanici,parola):
    if kullanici=="admin" and parola=="123456":
        return True
    else:
        return False
while True:
    kullanici_adi=input("Kullanıcı adınız:")
    parola=input("Parolanız:")
    if kontrolet(kullanici_adi,parola)==True:
        print("Giriş başarılı")
        break
    else:
        print("Başarısız giriş")

