#klavyeden q harfi girilene kadar girilen sayıları listeye atayan, en son
# q girildiğinde listeyi ekrana yazdıran kod

klavye=""
girilenler=[]

while klavye!="q":
    klavye=input("bir sayı giriniz")
    if klavye!="q":
        if klavye!="":
            girilenler.append(klavye)
print(girilenler)