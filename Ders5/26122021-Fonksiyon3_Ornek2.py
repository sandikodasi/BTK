def hesapla(x):
    if 85<x<100:      #x<=100 and x>=85:
        print("Taktir")
    elif x<85 and x>=75:
        print("teşekkür")
    else:
        print("Hiçbirşey alamadınız")
ortalama=int(input("Ortlamanızı giriniz"))
hesapla(ortalama)