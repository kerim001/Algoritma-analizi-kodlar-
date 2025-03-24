def insertion_sort(veri_dizisi):
   for index in range(1, len(veri_dizisi)):
       mevcut = veri_dizisi[index]  # Sıralanacak eleman
       pozisyon = index - 1
       
       # Mevcut elemandan daha büyük olanları ileriye taşı
       while pozisyon >= 0 and mevcut < veri_dizisi[pozisyon]:
           veri_dizisi[pozisyon + 1] = veri_dizisi[pozisyon]
           pozisyon -= 1
           
       # Mevcut elemanı uygun konuma yerleştir
       veri_dizisi[pozisyon + 1] = mevcut
   
   return veri_dizisi