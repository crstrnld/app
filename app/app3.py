def syarat_kelulusan(mtk, ipa, inggris):
    nilai = [mtk, ipa, inggris]
    rata_rata_nilai = sum(nilai) / len(nilai)
    dibawah_70 = sum(1 for nilai in nilai if nilai < 70)
    nilai_sempurna = any(nilai == 100 for nilai in nilai)

    if rata_rata_nilai > 75 and dibawah_70 <= 1 and nilai_sempurna: 
        return "lulus"
    else:
        return "gagal"
    
mtk = float(input("nilai mtk: "))
ipa = float(input("nilai ipa: "))
inggris = float(input("nilai inggris: "))

hasil = syarat_kelulusan(mtk, ipa, inggris)
print(f"hasil: {hasil}")


