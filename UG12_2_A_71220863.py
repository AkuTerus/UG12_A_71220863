masukan_kalimat = input("Masukan Nama : ")
muncul = 0 
for i in range(len(masukan_kalimat)):
    muncul +=1
    print(masukan_kalimat[:muncul]) 
for i in range(len(masukan_kalimat)):
    muncul -= 1
    print(masukan_kalimat[:muncul])