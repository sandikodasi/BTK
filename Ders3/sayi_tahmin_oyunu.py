import random
seviye=input("Bir seviye seçiniz (kolay/orta/zor):").lower()
if seviye=="kolay":
    sayi=random.randint(1,10)
elif seviye=="orta":
    sayi=random.randint(1,50)
elif seviye=="zor":
    sayi=random.randint(1,100)
while True:
    tahmin=int(input("Tahminiz:"))
    if tahmin==sayi:
        print("Tebrikler!")
        break
    elif tahmin>sayi:
        print("Sayınızı küçültün")
    else:
        print("Sayınızı büyütün")
    if seviye=="orta":
        sayi=random.randint(1,50)
        if tahmin==sayi:
            print("Tebrikler!")
            break
        elif tahmin>sayi:
            print("Sayınızı küçültün")
        else:
            print("Sayınızı büyütün")
    if seviye=="zor":
        sayi=random.randint(1,100)
        if tahmin==sayi:
            print("Tebrikler!")
            break
        elif tahmin>sayi:
            print("Sayınızı küçültün")
        else:
            print("Sayınızı büyütün")

#githuba yükle, sandikodasi altına, BTK baslıgı içine