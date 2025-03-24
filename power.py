def power(a, b):
   sonuc = 1
   taban = a  # İlk ekstra değişken
   kuvvet = b  # İkinci ekstra değişken
   
   while kuvvet > 0:
       sonuc *= taban
       kuvvet -= 1
   
   return sonuc


# Kullanım örneği
x = 2
y = 5
print(power(x, y))  # Sonuç: 32