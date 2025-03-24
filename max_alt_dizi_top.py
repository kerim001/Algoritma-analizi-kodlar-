#En Yüksek Alt Seri Toplamını Bulan Fonksiyon (Böl ve Yönet Stratejisi)
#Bu kod, bir sayı dizisindeki ardışık elemanların oluşturduğu en büyük toplama sahip alt diziyi bulur.
#Algoritmanın karmaşıklık analizi: O(n log n)

def max_subarray_sum(sayilar):
   def alt_fonksiyon(baslangic, bitis):
       if baslangic == bitis:
           return sayilar[baslangic]
       
       orta = (baslangic + bitis) // 2
       
       # Üç farklı durumu hesapla
       sol_toplam = alt_fonksiyon(baslangic, orta)
       sag_toplam = alt_fonksiyon(orta + 1, bitis)
       ortadan_gecen = max_crossing_sum(baslangic, orta, bitis)
       
       return max(sol_toplam, sag_toplam, ortadan_gecen)
   
   def max_crossing_sum(baslangic, orta, bitis):
       # Ortadan sola doğru maksimum toplamı bul
       sol_max = float('-inf')
       ara_toplam = 0
       for i in range(orta, baslangic - 1, -1):
           ara_toplam += sayilar[i]
           if ara_toplam > sol_max:
               sol_max = ara_toplam
       
       # Ortadan sağa doğru maksimum toplamı bul
       sag_max = float('-inf')
       ara_toplam = 0
       for i in range(orta + 1, bitis + 1):
           ara_toplam += sayilar[i]
           if ara_toplam > sag_max:
               sag_max = ara_toplam
       
       return sol_max + sag_max
   
   return alt_fonksiyon(0, len(sayilar) - 1)

# Test
test_dizisi = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("En yüksek ardışık toplam:", max_subarray_sum(test_dizisi))
# Sonuç: 6