# for i in range(1,100):
#     if i%2==0:
#         print(i)

# for i in range(2,100,2): # adım sayısı ile her bir adımdaki artışı ayarlayabiliriz
#     print(i)
# a=5
# while a<10: #şarta bağlı döngüdür.. şart gerçekleştiği sürece çalışır
#     print("Çok ÇALIŞ!!!")
#     a=a+1 #a+=1
# a=1
# while True:
#     print(a,"BAŞARACAĞIM!")
#     a=a+1
#     if a==10:
#         break #döngüyü sonlandırmak/kırmak için kullanılır

# aylar=["ocak","şubat","mart","nisan","mayıs","haziran"]
# for i in range(len(aylar)):
#     print(aylar[i])
#

# for i in aylar: # for döngüsü ile listeler üzerinde de işlem yapılabilir
#     print(i)















#Sonsuz döngü
# while True:
#     print("BTK")

#Döngü kırma

# while True:
#     isim=input("İsim(çıkmak için q giriniz):")
#     if isim=="q":
#         break #döngüyü sonlandırır

#Kullanıcıadı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak
#123456 girilince "sisteme başarıyla giriş yaptınız" yazsın..
#yanlış girildikçe "kullanıcıadı veya şifre hatalı" yazıp
#tekrar kullanıcıadı ve şifre sorsun!

while True:
    kullaniciadı=input("Kullanıcı adınız:")
    sifre=input("Parolanız:")
    if kullaniciadı=="admin" and sifre=="123456":
        break
    else:
        print("Kullanıcı adı veya parola hatalı")
print("sisteme başarıyla giriş yaptınız..")

