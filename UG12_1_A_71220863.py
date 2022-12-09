awal_deret = int(input("Masukan awal deret : "))
akhir_deret = int(input("Masukan Akhir deret : "))
for i in range(awal_deret,akhir_deret):
    if i%2==1 and i%3!=0 and i%6!=0:
        print(i,end=" ")

