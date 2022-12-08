
######## Kodingan dalam bentuk fungsi ########
#Materi 1.
def materi1a():
    print('1.a. Memahami Perulangan "While"')
    print("""\nPerintah while adalah perintah yang akan mengulang mengeksekusi statemen dalam blok while selama nilai kondisinya TRUE. Dan akan baru berhenti mengulangi eksekusi blok statemen while apabila kondisinya FALSE. Rumus umum statemen while:
          while(kondisi):
                statemen""")
def materi1b():
    print("1.b. Contoh while dan latihan while 1-3")
    xyz=0
    while(xyz<10):
        print('Ini perulangan ke -',xyz)
        xyz+=1
    #Materi1Latihan1
    def materi1latihan1():
        lat1while=0
        while(lat1while<5):
            print('Teknik Informatika UNISNU Jepara')
            lat1while+=1
    #Materi1Latihan2
    def materi1latihan2():
        lat2while=0
        while(lat2while<3):
            print("Program Studi Teknik Informatika")
            print("Fakultas Sains dan Teknologi Jepara")
            lat2while+=1
    #Materi1Latihan3
    def materi1latihan3():
        lat3while=0
        while(lat3while<3):
            print("Program Studi Teknik Informatika".center(40,' '))
            lat3while+=1
        lat3while2=0
        while(lat3while2<5):
            print("Fakultas Sains dan Teknologi".center(40,' '))
            lat3while2+=1
        lat3while3=0
        while(lat3while3<5):
            print("Universitas Islam Nahdlatul Ulama Jepara".center(40,' '))
            lat3while3+=1
    materi1latihan1()
    materi1latihan2()
    materi1latihan3()
def materi1c():
    print("1.c. Perulangan While dengan Input")
    teksInput=input('Masukkan teks yang ingin difotocopy: ')
    berapakali=int(input('Masukkan berapa kali ingin difotocopy teks tersebut: '))
    while 0<berapakali:
        print(teksInput)
        berapakali-=1
def materi1d():
    print('1.d. Contoh while dengan input dan latihan')
    a=int(input('Masukkan berapa kali pencetakan : '))
    angka=0
    while(angka<a):
        print('Prodi Teknik Informatika Fakultas Sains dan Teknologi UNISNU Jepara')
        angka+=1
    print('1.d. Latihan 1.d.')
    print(' Program Perulangan While dengan Inputan '.center(40,'-'))
    kalimat=input('Masukkan kalimat yang ingin dicetak : ')
    kalimatBerapaKali=int(input('Masukkan berapa kali pencetakan     : '))
    varw=0
    while(kalimatBerapaKali>varw):
        print(kalimat)
        kalimatBerapaKali+=1
def materi2a():
    print('2.a. Materi 2: BREAK (Statement break)')
    print("- Statemen Break -")
    print("Statemen break digunakan untuk keluar dari perulangan, misalnya keluar dari perulangan walaupun kondisi perulangan masih TRUE atau rangkaiannya belum diselesaikan atau teriterasi seluruhnya.")
    print(' Contoh program perulangan while dengan break '.center(40,'-'))
    print('Program ini akan berhenti jika kalian mengetik "keluar".')
    while True:
        data=input('Masukkan string sembarang: ')
        if data=='keluar':
            break
        print('Inputan pengguna',data)
    print('Selesai')
def materi2b():
    print('2.b. Materi 2: BREAK (Perbedaan break dengan exit)')
    print('Jika break menghentikan perulangan, maka exit akan menghentikan program, secara keseluruhan.')
    print(' Contoh program perulangan while dengan exit '.center(40,'-'))
    print('Program ini akan berhenti jika kalian mengetik "keluar" atau benar-benar berhenti jika "stop".')
    while True:
        data=input('Masukkan string sembarang: ')
        if data=='keluar':
            exit()
        elif data=='stop':
            exit()
        print('Inputan pengguna',data)
def main():
    print('Ini adalah hasil pekerjaan Sidra Febrian Hardiyanto untuk materi Pemrograman Terstruktur pertemuan ke-12-13')
    print("""
    SIDRA FEBRIAN HARDIYANTO
    221240001231
    Daftar isi
        1. Materi 1: WHILE
            a. Perulangan While
            b. Contoh while dan latihan while 1-3
            c. Perulangan While dengan Input
            d. Contoh while dengan input dan latihan
            e. TUNJUKKAN SEMUA MATERI 1
        2. Materi 2: BREAK
            a. Statement break
            b. Perbedaan break dengan exit
            c. TUNJUKKAN SEMUA MATERI 2
        3. Materi: SEMUA MATERI DI ATAS
    """)
def materi():
    pilihMateri=int(input("Pilih materi yang ingin dilihat. (1/2) -> "))
    if pilihMateri==1:
        pilihMateri2=input("Pilih sub-materi 1 yang ingin dilihat. (a/b/c/d) -> ")
        if pilihMateri2=='a':
            materi1a()
        elif pilihMateri2=='b':
            materi1b()
        elif pilihMateri2=='c':
            materi1c()
        elif pilihMateri2=='d':
            materi1d()
        elif pilihMateri2=='e':
            materi1a()
            materi1b()
            materi1c()
            materi1d()
    if pilihMateri==2:
        pilihMateri2=input("Pilih sub-materi 2 yang ingin dilihat. (a/b) -> ")
        if pilihMateri2=='a':
            materi2a()
        elif pilihMateri2=='b':
            materi2b()
        elif pilihMateri2=='c':
            materi2a()
            materi2b()
    if pilihMateri==3:
        materi1a()
        materi1b()
        
main()
materi()
ulangMateri=input('Mau diulang kembali? (y/g) ')
while ulangMateri=='y':
    materi()
    ulangMateri=input('Mau diulang kembali? (y/g) ')
    if ulangMateri=='g':
        exit()
