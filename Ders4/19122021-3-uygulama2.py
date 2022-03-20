#Kullanıcı adını ve parolasını sorsun, admin ve parolaya 123456 yazılınca
# hoşgeldin desin. Admin ve 123456 yazılmadığı sürece
# tekrar kullanıcı adı ve parola istesin(sürekli)
dosya=open("girisler.txt", "w",encoding="utf-8")
kullanici=""
parola=""
while kullanici!="admin" or parola!="123456":
    kullanici=input("Kullanıcı adınız: ").lower()
    parola=input("Parolanız:")
    if kullanici=="admin" and parola=="123456":
        print("Hoşgeldin")
        dosya.write("Başarıyla giriş yapıldı..\n")
    else:
        print("Kullanıcıadı veya parolanız hatalı")
print("Sisteme giriş yapıldı")
dosya.close()