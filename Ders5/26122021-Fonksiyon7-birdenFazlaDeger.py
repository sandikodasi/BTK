#kendisine gönderilen tüm değerleri, toplayıp ekrana basan fonksiyon
#3 tanede gönderilebilir, 5 tanede, 10 tanede ....


def topla(*sayilar): #gonderilen tüm değerler sayilar adında bir demete atandı
    toplam=0
    for i in sayilar:
        toplam=toplam+i #toplam+=i
    print(toplam)


topla(3,5,6,15,67)