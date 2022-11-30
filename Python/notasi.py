print("Ini adalah program menghitung bilangan baris dan deret aritmatika dan geometri")
print("""Program ini dapat menghitung:
1. Bilangan baris dan deret Aritmatika (+)
2. Bilangan baris dan deret Geometri (x)

Rumus
1. Aritmatika
    UnAritmatika=a+(n-1)*b
    SnAritmatika=n/2*(2*a+(n-1)*b)
2. Geometri
    UnGeometri=a*(r**(n-1))
    SnGeometri=(a*(r**n)-1)/(r-1)""")
pilihan=int(input("Masukkan angka 1 atau 2 untuk memilih rumus yang akan dihitung : "))
if pilihan==1:
    print(" - Aritmatika - ".center(60,"A"))
    a=int(input("\nMasukkan a : "))
    b=int(input("Masukkan b : "))
    n=int(input("Masukkan n : "))
    UnAritmatika=a+(n-1)*b
    SnAritmatika=n/2*(2*a+(n-1)*b)
    print("Nilai Un = ",UnAritmatika)
    print("Nilai Sn = ",SnAritmatika)
elif pilihan==2:
    print(" - Geometri - ".center(60,"G"))
    a=int(input("\nMasukkan a : "))
    r=int(input("Masukkan r : "))
    n=int(input("Masukkan n : "))
    UnGeometri=a*(r**(n-1))
    SnGeometri=(a*(r**n)-1)/(r-1)
    print("Nilai Un = ",UnGeometri)
    print("Nilai Sn = ",SnGeometri)
else:
    print("Input error.")