print("Ini adalah program menghitung bilangan baris dan deret aritmatika dan geometri")
print("wk"*10)
kata=" "
print(kata.center(60,"="))
print("""Program ini dapat menghitung:
1. Notasi Aritmatika (+)
2. Notasi Geometri (x)

Rumus
1. Aritmatika
    Un=a+(n-1)b
    Sn=n/2(2*a+(n-1)b)
2. Geometri
    UnGeometri=a*(r**n-1)
    SnGeometri=(a*(r**n)-1)/(r-1)
""")
pilihan=int(input("Masukkan angka 1 atau 2 untuk memilih rumus yang akan dihitung : "))
if pilihan==1:
    a=int(input("Masukkan a : "))
    b=int(input("Masukkan b : "))
    n=int(input("Masukkan n : "))
    UnAritmatika=a+(n-1)*b
    SnAritmatika=n/2*(2*a+(n-1)*b)
    print("Nilai Un = ",int(UnAritmatika))
    print("Nilai Sn = ",int(SnAritmatika))
elif pilihan==2:
    a=int(input("Masukkan a : "))
    r=int(input("Masukkan r : "))
    n=int(input("Masukkan n : "))
    UnGeometri=a*(r**(n-1))
    SnGeometri=(a*(r**n)-1)/(r-1)
    print("Nilai Un = ",UnGeometri)
    print("Nilai Sn = ",SnGeometri)
else:
    print("Input error.")