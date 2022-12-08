print(" MATERI LOOPING FOR & RANGE ".center(80,"!"))
print("!"*80)
print("\nSIDRA FEBRIAN HARDIYANTO 221240001231 DA TIF UNISNU")
for i in [1,2,3,4,5]:
    print("Pengulangan for ke - ",i)

print("\n")
Matrix = [(1,2),(3,4),(5,6)]
for (a,b) in Matrix:
    print((a,b))

print("\n")
for xyz in "x","y","z":
    print(xyz, "adalah alfabet")

print("\n")
deret=['pertama','kedua','ketiga',"keempat","kelima","keenam"]
for ke in deret:
    print("Urutan bilangan",ke)

print("\n")
print(" - Latihan 1 - ".center(40,'L'))
makananJepara=["Pindang Srani",'Sayur Bening','Sayur Sop','Kupat Ndog','Lontong Sayur','Kacang Open']
for mangan in makananJepara:
    print(mangan,'adalah masakan khas dari Jepara')
print("\n")
print(" - Latihan 2 - ".center(40,'L'))
dataLatihan2=[('Alan',13,'ngewibu','Jepara'),('Amirul',69,'nyari promo','mana saja'),('Abi',18,'otomotif','Pati'),('AkuSiapa',666,'gak tahu coy','hatimu')]
for(nama,usia,hobi,tinggal) in dataLatihan2:
    print("Nama saya",nama,"usia saya",usia,"tahun dan hobi saya",hobi,"adalah sebuah hobi yang sangat menyenangkan bagi saya. Btw saya tinggal di",tinggal,"yagesya.\n")
print("\n")
print("!"*80)
print(" MATERI RANGE ".center(80,"!"))
print("!"*80)
# Python berhitung mulai dari 0 yagesya, bukan 1, kalau 1 itu kamu, hanya ada satu di hatiku hiya hiya >///<
print("\n")
for iniApaYa in range(8):
    print(iniApaYa)    
print("\n")
for iniApaYa2 in range(1,9):
    print(iniApaYa2)
else:
    print("Programnya dah kelar cuy, dah sampe", iniApaYa2)
print("\n")
namaBuatPraktikRange=['Emir','Sultan','Khalif','Sayyid','Imam']
umurBuatPraktikRange=[20,21,22,23,24]
for urutan in range(len(umurBuatPraktikRange)):
    print(namaBuatPraktikRange[urutan],'berusia',umurBuatPraktikRange[urutan],'tahun.')
print("\n")
print(range(1,10,2))
print("\n")
print(" - Latihan Range sama For - ".center(40,'L'))
for latihanRange in range(1,10,2):
    # maksudnya tuh gini, buat variabel latihanRange, mulai dari 1, stop sampai 10, inkremen 2
    print('Nilai rata-rata mahasiswa semester',latihanRange,'adalah 85')
print("\n")
mulaiDari=int(input('Masukkan range untuk mulaiDari : '))
sampaiDengan=int(input('Masukkan range untuk sampaiDengan : '))
kelipatan=int(input('Masukkan range untuk kelipatan : '))
for variabelRANGE in range(mulaiDari,sampaiDengan,kelipatan):
    print('Variabel range ke - ',variabelRANGE)
print("""\nCara menggunakan range:
for variabelRANGE in range(mulaiDari,sampaiDengan,kelipatan):
    print('Variabel range ke - ',variabelRANGE)
Misalnya nih...
--------- Inputnya begini: ---------
for variabelRANGE in range(1,10,2):
    print('Variabel range ke - ',variabelRANGE)
--------- Outputnya jadi: ---------
Variabel range ke -  1
Variabel range ke -  3
Variabel range ke -  5
Variabel range ke -  7
Variabel range ke -  9

Artinya: 
user: buat variabelRANGE terus print mulai dari 1 sampai 10 tapi kelipatan 2
komputer: ok, variabelRANGE= 1-10;
                             1,1+2,3+2,5+2,7+2;
                             1,3,5,7,9
Nggak sampai 9+2 karena sampai dengan 10 saja
""")
print("\n")
print("!"*80)
print(" MATERI PERULANGAN FOR DENGAN VALUE INPUT ".center(80,"!"))
print("!"*80)
print("\n")
inputPerulangan=int(input("Program ini pengen ketawa. Masukkan sampai berapa kali dia dibolehin ketawa : "))
for ketawa in range(inputPerulangan):
    print("akwkawkwk ketawa ke -",ketawa+1)
print("\n")
print(" - Latihan Range sama For dengan Input 1 - ".center(40,'L'))
inputLatihanforrangeinput=int(input('Mau dicopy berapa kali ini tulisan "TIF UNISNU Jepara"? -> '))
for copyBrpX in range(inputLatihanforrangeinput):
    print('TIF UNISNU Jepara')
print("\n")
print(" - Latihan Range sama For dengan Input 2 - ".center(40,'L'))
inputLatihanforrangeinput21=input('Mau fotocopy? Masukkin string yang mau difotocopy -> ')
inputLatihanforrangeinput22=int(input('Mau dicopy berapa kali ini tulisannya? -> '))
for fotocopy in range(inputLatihanforrangeinput22):
    print(inputLatihanforrangeinput21)
print("\n")
print(" - Latihan Range sama For dengan Input 3 - ".center(40,'L'))
print("\n")
namaRangeInput3=input('Masukkan nama mahasiswa yang ingin difotocopy -> ')
nimRangeInput3=int(input('Masukkan NIM yang ingin difotocopy ->'))
IPKRangeInput3=int(input('Masukkan IPK mahasiswa yang ingin difotocopy -> '))
brpnamaRangeInput3=int(input('\nMasukkan berapa kali nama mahasiswa difotocopy -> '))
brpnimRangeInput3=int(input('Masukkan berapa kali NIM difotocopy ->'))
brpIPKRangeInput3=int(input('Masukkan berapa kali IPK mahasiswa difotocopy -> '))
print("\n")
for bingungNamainVariabelnyaApa1 in range(brpnamaRangeInput3):
    print(namaRangeInput3)
print("\n")
for bingungNamainVariabelnyaApa2 in range(brpnimRangeInput3):
    print(nimRangeInput3)
print("\n")
for bingungNamainVariabelnyaApa3 in range(brpIPKRangeInput3):
    print(IPKRangeInput3)
print("")