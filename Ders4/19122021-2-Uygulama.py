#Kullanıcı adını sorsun, admin yazılınca hoşgeldin desin. Admin yazılmadığı sürece
# tekrar kullanıcı adı istesin(sürekli)

kullanici=""#while'ın şartında kullanabilmek için burada tanımlamak zorundayım!
while kullanici!="admin":
    kullanici=input("Kullanıcı adınız: ").lower()
    if kullanici=="admin":
        print("Hoşgeldin")
print("Sisteme giriş yapıldı")
