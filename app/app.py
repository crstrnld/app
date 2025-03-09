def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

tahun = int(input("masukan tahun: "))
if tahun_kabisat(tahun):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} adalah tahun kabisat.")
