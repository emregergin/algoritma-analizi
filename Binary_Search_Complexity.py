import random
import time


# Binary Search algoritması
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Eleman bulundu
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Eleman bulunamadı


# Binary Search algoritmasının çalıştığı süreyi ölçen fonksiyon
def measure_binary_search_time(arr, target):
    start_time = time.perf_counter()  # Daha hassas zaman ölçümü
    binary_search(arr, target)
    end_time = time.perf_counter()
    return end_time - start_time


# Deneysel analiz yapıp Binary Search'ün karmaşıklığını yazdıran fonksiyon
def experimental_analysis(arr_sizes):
    for size in arr_sizes:
        arr = sorted(random.sample(range(1, size * 10), size))  # Sıralı bir dizi oluştur
        target = random.choice(arr)  # Diziden rastgele bir hedef eleman seç

        # Binary Search için zaman ölçümü
        elapsed_time = measure_binary_search_time(arr, target)

        # Zaman karmaşıklığına dair bilgi yazdır
        print(f"Array size: {size}, Binary Search time: {elapsed_time:.10f}s")
        print("Theoretical time complexity: O(log n)")
        print("-" * 50)


# Örnek dizi boyutları
arr_sizes = [10000, 50000, 100000, 200000, 500000]

# Deneysel analizi çalıştır
experimental_analysis(arr_sizes)
