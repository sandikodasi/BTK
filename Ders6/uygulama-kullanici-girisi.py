#Kullanıcı adını ve parolasını sorsun, admin ve parolaya 123456 yazılınca
# hoşgeldin desin. Admin ve 123456 yazılmadığı sürece
# tekrar kullanıcı adı ve parola istesin(sürekli)
import datetime
dosya=open("girisler.txt","a",encoding="utf-8")
kullanici=""
parola=""
while kullanici!="admin" or parola!="123456":
    kullanici=input("Kullanıcı adınız: ").lower()
    parola=input("Parolanız:")
    giris=datetime.datetime.now()
    if kullanici=="admin" and parola=="123456":
        print("Hoşgeldin")
        dosya.write(str(giris)+" tarihinde başarılı giriş yapıldı\n")


    else:
        print("Kullanıcıadı veya parolanız hatalı")

        dosya.write("Kullanıcıadı:"+kullanici+" Password:"+parola+" denenerek "+str(giris)+ "tarihinde başarısız giriş\n")
print("Sisteme giriş yapıldı")
dosya.close()