def diskon(pembelian):
    if pembelian > 100000:
        diskon = 0.10
    if pembelian > 50000:
        diskon = 0.05
    else:
        diskon = 0.0

    pembelian = pembelian * (1 - diskon)
    return pembelian
    
pembelian = float(input("masukan jumlah pembelian: "))
diskon_total = diskon(pembelian)
print(f"jumlah yang dibayar setelah diskon adalah: {diskon_total}")





