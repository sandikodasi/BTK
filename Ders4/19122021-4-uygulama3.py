#klavyeden q harfi girilene kadar girilen sayıları listeye atayan, en son
# q girildiğinde listeyi ekrana yazdıran kod










klavye=""
girilenler=[]

while klavye!="q":
    klavye=input("bir sayı giriniz")
    if klavye!="q":
        if klavye!="": #hiçbirşey yazmadan enter'a bastığımızda listeye boşluk eklemesin diye bu sorguyu yaptık
            try:
                girilenler.append(int(klavye)) #boşluk veya q dğeilse listeye ekledik
            except ValueError:
                print("Sadece sayı girmelisiniz!")
print(girilenler) # girilenler listemizi yazdırdık