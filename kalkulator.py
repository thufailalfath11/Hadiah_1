def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 != 0:
        return angka1 / angka2
    else:
        print("Error: Tidak bisa membagi dengan nol")

print("Selamat datang di Kalkulator Sederhana")
print("=====================================\n")

while True:
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan (0-4): ")

    if pilihan == '0':
        print("Terima kasih telah menggunakan kalkulator ini.")
        break

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = tambah(angka1, angka2)
        print("Hasil: ", hasil)
    elif pilihan == '2':
        hasil = kurang(angka1, angka2)
        print("Hasil: ", hasil)
    elif pilihan == '3':
        hasil = kali(angka1, angka2)
        print("Hasil: ", hasil)
    elif pilihan == '4':
        hasil = bagi(angka1, angka2)
        if hasil is not None:
            print("Hasil: ", hasil)
    else:
        print("Error: Pilihan yang dimasukkan tidak valid")
