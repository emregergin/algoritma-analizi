import random
import time


# Bubble Sort algoritması
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Elemanları yer değiştir


# Bubble Sort algoritmasının çalıştığı süreyi ölçen fonksiyon
def measure_bubble_sort_time(arr):
    start_time = time.time()
    bubble_sort(arr)
    return time.time() - start_time


# Deneysel analiz yapıp Bubble Sort'un karmaşıklığını yazdıran fonksiyon
def experimental_analysis(arr_sizes):
    for size in arr_sizes:
        arr = random.sample(range(1, size * 10), size)  # Rastgele bir dizi oluştur

        # Bubble Sort için zaman ölçümü
        elapsed_time = measure_bubble_sort_time(arr)

        # Zaman karmaşıklığına dair bilgi yazdır
        print(f"Array size: {size}, Bubble Sort time: {elapsed_time:.5f}s")
        print("Theoretical time complexity: O(n^2)")
        print("-" * 50)


# Örnek dizi boyutları
arr_sizes = [100, 500, 1000, 2000, 5000]

# Deneysel analizi çalıştır
experimental_analysis(arr_sizes)
