import random
import time


# Bubble sort algoritması
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Elemanları yer değiştir


# Deneysel analiz yapmak için fonksiyon
def experimental_analysis(arr_sizes):
    results = []

    for size in arr_sizes:
        arr = random.sample(range(1, size * 10), size)  # Rastgele bir dizi oluştur

        # Bubble sort için zaman ölçümü
        start_time = time.time()
        bubble_sort(arr)
        bubble_sort_time = time.time() - start_time

        results.append((size, bubble_sort_time))
        print(f"Array size: {size}, Bubble Sort time: {bubble_sort_time:.5f}s")

    return results


# Örnek parametreler
arr_sizes = [100, 500, 1000, 5000, 10000]  # Farklı dizi boyutları

# Deneysel analizi çalıştır
results = experimental_analysis(arr_sizes)
