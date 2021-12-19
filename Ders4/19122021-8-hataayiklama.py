#print(a) #nameerror hatası
#print("Btk"deneme) syntax error
# print(5/0) #zeroDivisionError hatası verir
# int("5a") #valueError hatası verir
try: #hata verebilecek kodlar bu blok içine yazılır
    sayi1=int(input("1. sayıyı giriniz"))
    sayi2=int(input("2. sayıyı giriniz"))
    print(sayi2+sayi1)
except ValueError:
    print("Lütfen bir sayı giriniz!")
except ZeroDivisionError:
    print("Bir sayı 0 a bölünemez!")
# except:
#     print("Burası genel hata mesajı")
print("Program buradan çalışmasına devam eder!")