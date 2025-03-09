def bilangan(nilai):
    if nilai > 0:
        return "positif"
    elif nilai < 0:
        return "negatif"
    else:
        return "nol"
    
nilai = float(input("masukan nilai bilangan: "))
print(f"bilangan tersebut adalah {bilangan(nilai)}")


