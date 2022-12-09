batas_angka = int(input("Masukan Pembatas : "))
angka_terlarang = int(input("Masukan Angka terlarang : "))
for i in range(batas_angka):
    if i == angka_terlarang:
        continue
    print(i,end=" ")
