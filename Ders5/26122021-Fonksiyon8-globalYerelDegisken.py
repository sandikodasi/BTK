b=20 #global değişkendir
def fonksiyon():
    global b #dışarıdaki bir değişkeni fonksiyon içinde kullanabiliriz,
    # değerini değiştirebiliriz
    a=10 #yerel değişkendir. sadece fonksiyonun içinde
    print(b)
# print(a) #a değişkeni fonksiyonun içinde olduğu için kullanamayız,
# yerel değişken!
fonksiyon()
print(b) #global olarak tanımladığımız için ekrana 4 yazar
# eğer global b demeseydik ekrana 20 basardı
