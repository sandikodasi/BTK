#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek
#sonucunda True ya da False gönderen fonksiyonun python kodu
#kullanıcıadı: admin, şifre:123456 olmalı

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

