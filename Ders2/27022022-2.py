sayi1=int(input("1. sayıyı giriniz")) #inputtan girilen değerler "string" tipindedir.
sayi2=int(input("2. sayıyı giriniz")) #başa int ekleyerek integer dönüşüm yaptık
#print(sayi1+sayi2)
#toplama yapabilmek için string değeri integer'a çevirmek gerekir.
#print(int(sayi1)+int(sayi2))
print("Sayılarınızın toplamı:",sayi1+sayi2)
print("Sayılarınızın çarpımı:",sayi1*sayi2)
print("Sayılarınızın farkı:",sayi1-sayi2)
print("Sayılarınızın bölümü:",sayi1/sayi2)
print("Sayılarınızın bölümü:",sayi1//sayi2) #tam bölme yapar
print("1. sayı üzeri 2. sayı:",sayi1**sayi2)
print(sayi1,"in", sayi2, "ye bölümünden kalan",sayi1%sayi2, "dır")