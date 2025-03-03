import random
import time


# Birinci yöntem: Diziyi sıralayıp k. en küçük elemanı al
def method_1(arr, k):
    arr_sorted = sorted(arr)
    return arr_sorted[k - 1]


# İkinci yöntem: Sadece k elemanını sıralayıp kalanları karşılaştırmak
def method_2(arr, k):
    # İlk k elemanını seç ve sıralarız
    k_smallest = arr[:k]
    k_smallest.sort()

    # Kalan elemanları kontrol et
    for num in arr[k:]:
        if num < k_smallest[-1]:
            k_smallest[-1] = num
            k_smallest.sort()  # Sadece son elemana göre sıralarız

    return k_smallest[-1]


# Deneysel analiz yapmak için fonksiyon
def experimental_analysis(arr_sizes, k):
    results = {'method_1': [], 'method_2': []}

    for size in arr_sizes:
        arr = random.sample(range(1, size * 10), size)  # Rastgele bir dizi oluştur

        # method_1 için zaman ölçümü
        start_time = time.time()
        method_1(arr, k)
        method_1_time = time.time() - start_time

        # method_2 için zaman ölçümü
        start_time = time.time()
        method_2(arr, k)
        method_2_time = time.time() - start_time

        results['method_1'].append(method_1_time)
        results['method_2'].append(method_2_time)

        print(f"Array size: {size}, Method 1 time: {method_1_time:.5f}s, Method 2 time: {method_2_time:.5f}s")

    return results


# Örnek parametreler
arr_sizes = [100, 500, 1000, 5000, 10000]  # Farklı dizi boyutları
k = 50  # k. en küçük eleman

# Deneysel analizi çalıştır
results = experimental_analysis(arr_sizes, k)
