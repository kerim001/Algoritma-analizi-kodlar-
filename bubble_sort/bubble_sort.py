def bubble_sort(dizi):
    uzunluk = len(dizi)
    for dis_indeks in range(uzunluk):
        degisiklik_var = False
        for ic_indeks in range(uzunluk - dis_indeks - 1):
            if dizi[ic_indeks] > dizi[ic_indeks + 1]:
                # Elemanların yerini değiştir
                dizi[ic_indeks], dizi[ic_indeks + 1] = dizi[ic_indeks + 1], dizi[ic_indeks]
                degisiklik_var = True
        
        # Erken çıkış optimizasyonu - eğer bu geçişte hiç değişiklik olmadıysa
        # dizi zaten sıralıdır
        if not degisiklik_var:
            break
    
    return dizi