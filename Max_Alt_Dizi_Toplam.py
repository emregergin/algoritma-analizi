def maksimum_alt_dizi(arr):
    en_buyuk_toplam = arr[0]
    mevcut_toplam = arr[0]
    baslangic = 0
    bitis = 0
    for i in range(1, len(arr)):
        if mevcut_toplam + arr[i] > arr[i]:
            mevcut_toplam += arr[i]
        else:
            mevcut_toplam = arr[i]
            baslangic = i
        if mevcut_toplam > en_buyuk_toplam:
            en_buyuk_toplam = mevcut_toplam
            bitis = i
    return arr[baslangic:bitis+1], en_buyuk_toplam

# Örnek kullanım
dizi = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
alt_dizi, toplam = maksimum_alt_dizi(dizi)
print("Maksimum toplamlı alt dizi:", alt_dizi)
print("Toplam:", toplam)
