def insertion_sort(arr):
    for i in range(1, len(arr)):  # Dizinin ikinci elemanından başlayarak ilerler
        key = arr[i]  # Sıralı kısma eklenmek istenen öğe
        j = i - 1
        # 'key' değeri ile sıralı kısımdaki öğeleri karşılaştırır ve uygun konumu bulur
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Öğeleri sağa kaydırır
            j -= 1
        arr[j + 1] = key  # 'key' değerini doğru konumuna yerleştirir
    return arr

# Örnek kullanım
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sıralanmış dizi:", sorted_arr)
