def max_subarray(liste):
   en_buyuk = liste[0]
   suanki = liste[0]
   
   for indeks in range(1, len(liste)):
       # Ya yeni elemandan başla ya da mevcut toplamı devam ettir
       suanki = max(liste[indeks], suanki + liste[indeks])
       # Genel maksimumu güncelle
       en_buyuk = max(en_buyuk, suanki)
   
   return en_buyuk


# Kullanım örneği
sayilar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(sayilar))  # Sonuç: 6