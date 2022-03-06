"""
kullanıcı yılsonu ortalaması girsin. ortalama 85 üstü ise taktir, 70 üstü teşekkür,
bunların dışında ise hiçbir belge alamadınız desin..
"""
ortalama=int(input("Yılsonu ortalamanız:"))
if ortalama>=85:
    print("Taktir belgesi aldınız")
elif ortalama>=70:
    print("Teşekkür belgesi aldınız")
else:
    print("Hiçbir belge alamadınız")