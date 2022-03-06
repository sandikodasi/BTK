import time
dosya=open("bilgiler.txt","r",encoding="utf-8")
icerik=dosya.read()
print("içerik okunuyor...")

time.sleep(3)
print(icerik)
dosya.close()