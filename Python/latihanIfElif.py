"""
SIDRA FEBRIAN HARDIYANTO
221240001231
PEMROGRAMAN TERSTRUKTUR
ELIF 
"""

print("Apakah kamu ingin menjadi anime?\n")
n = input("Yakin (y/t)")
if n=="y":
    print("Baiklah, dalam 5 menit akan ada truck yang mengantarkanmu menuju isekai")
    print(". . .")
    print("BRRUUUUUUUAAAAAAAAAAKKKKKKKKKKK")
    print("SELAMAT DATANG DI ISEKAI")
elif n=="t":
    print("Dih gak asik luwh bang")
    print("Ya udah gw gak mau temenan sama luwh")
else:
    if n=="x":
        print("y apa t woigh")
    else:
        print("Disuruh input y/t malah input yang lain, hadeh hadeh")




print("================ Latihan Elif ================")
print("\nBuatlah program menentukan keterangan nilai ujian dengan statemen if else elif:")
namaMahasiswa=input("Masukkan nama mahasiswa :")
nilaiMahasiswa=int(input("Masukkan nilai ujian mahasiswa  : "))

if nilaiMahasiswa>=85:
    print("\nNilai mahasiswa",namaMahasiswa,"A karena memiliki nilai ujian",nilaiMahasiswa)
elif nilaiMahasiswa>=75:
    print("\nNilai mahasiswa",namaMahasiswa,"B karena memiliki nilai ujian",nilaiMahasiswa)
elif nilaiMahasiswa>=60:
    print("\nNilai mahasiswa",namaMahasiswa,"C karena memiliki nilai ujian",nilaiMahasiswa)
elif nilaiMahasiswa>=50:
    print("\nNilai mahasiswa",namaMahasiswa,"D karena memiliki nilai ujian",nilaiMahasiswa)
elif nilaiMahasiswa<=49:
    print("\nNilai mahasiswa",namaMahasiswa,"E karena memiliki nilai ujian",nilaiMahasiswa)
else:
    print("Sepertinya nilai mahasiswa mengalami error, silakan cek kembali inputnya, atau kodingan dalam sistem.")
print("================ Latihan Elif 2 ================")
print("Buatlah program menghitung luas persegi panjang, segitiga, lingkaran dengan statemen if elif else:\n - Jika pilih 1 maka menghitung uas persegi panjang\n - Jika pilih 2 maka menghitung luas segitiga\n - Jika pilih 3 maka menghitung luas lingkaran\n - Jika pilihannya selain ketiga di atas maka print error prompt.")

print("\n\nPilihan program yang tersedia:\n1. Program menghitung luas persegi panjang\n2. Program menghitung luas segitiga\n3. Program menghitung luas lingkaran")
programMana=int(input("\n\nMasukkan piliha program menurut angka di atas (1/2/3) : "))

if programMana==1:
    print("Anda memilih program penghitung luas persegi panjang")
    panjangPP=float(input("Masukkan panjang Persegi Panjang : "))
    lebarPP=float(input  ("Masukkan lebar Persegi Panjang   : "))
    luasPP=panjangPP*lebarPP
    print("Luas persegi panjang dengan panjang dihitung dengan",panjangPP,"x",lebarPP,"=",luasPP)
elif programMana==2:
    print("Anda memilih program penghitung luas segitiga")
    alasSG=float(input("Masukkan alas segitiga : "))
    tinggiSG=float(input  ("Masukkan tinggi segitiga : "))
    luasSG=(alasSG*tinggiSG)/2
    print("Luas segitiga dihitung dengan cara 0.5 dikalikan alas",alasSG,"dikalikan tinggi",tinggiSG,"=",luasSG)
elif programMana==3:
    print("Anda memilih program penghitung luas lingkaran")
    jarijariL=float(input("Masukkan jari-jari lingkaran : "))
    luasLingkaran=float(3.14*jarijariL*jarijariL)
    print("Luas lingkaran dihitung dengan cara 3.14 dikalikan jari-jari",jarijariL,"kuadrat = ",luasLingkaran)
else:
    print("Mohon untuk memasukkan pilihan 1, 2, atau 3")

print('='*60)
n=input('Masukkan huruf/angka/simbol -> ')
if not n: #Jika n kosong
    print('Anda tidak memasukkan apapun.')
else:
    print('String yang dimasukkan adalah:\n'+n)
print('='*60)
unameDB='admin'
pwDB='admin'
uname=input('Masukkan username : ')
pw=input('Masukkan password  : ')
if uname==unameDB and pw==pwDB:
    print('Selamat datang',uname)
elif uname !=unameDB and pw!=pwDB:
    print('Username dan password yang anda masukkan tidak cocok.')
else:
    print('Anda belum memasukkan username dan password.')

uname=input('Masukkan username : ')
pw=input('Masukkan password  : ')
if uname==unameDB or pw==pwDB:
    print('Selamat datang',uname)
elif uname!=unameDB or pw!=pwDB:
    print('Username dan password yang anda masukkan tidak cocok.')
else:
    print('Anda belum memasukkan username dan password.')