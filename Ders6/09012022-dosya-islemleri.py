dosya=open("bilgiler.txt","w",encoding="utf-8") #türkçe karakterler için utf-8 i ekledim
#w kipi dosyayı her seferinde yeniden oluşturur.
#a kipi: dosya yoksa yeniden oluşturur, var ise açıp en son satırdan ekleme yapar
#r kipi: dosyayı sadece okumak için açar
dosya.write("BTK\n")
dosya.write("Ankara\n")
dosya.write("çğıüş\n")
dosya.close()