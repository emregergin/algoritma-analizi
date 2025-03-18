def us_alma(sayi, us):
    return sayi ** us

# Kullanıcıdan taban ve üs değerlerini alalım
try:
    taban = int(input("Üssü alınacak sayıyı girin: "))
    üs = int(input("Üs değerini girin: "))
    # Fonksiyonu çağırarak sonucu hesaplayalım
    sonuc = us_alma(taban, üs)
    print(f"{taban} ^ {üs} = {sonuc}")
except ValueError:
    print("Lütfen geçerli bir sayı ve tam sayı değeri girin.")
