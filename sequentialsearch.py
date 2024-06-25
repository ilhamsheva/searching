import os

def sequential(jenis_barang, target_barang):
    for index, barang in enumerate(jenis_barang):
        if barang == target_barang:
            return index
    return -1

def tambah_barang(daftar_barang, barang_baru):
    daftar_barang.append(barang_baru)
    print(f"Barang {barang_baru} berhasil ditambahkan!")

daftar_barang = ['kemeja', 'celana', 'jaket', 'kacamata', 'sepatu']

while True:
    print("============================================")
    print("PROGRAM PENCARIAN BARANG (SEQUENTIAL SEARCH)")
    print("============================================\n")
    print("1. Tampilkan Barang-Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang")
    print("4. Exit")
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        print("Daftar barang saat ini:")
        for barang in daftar_barang:
            print(barang)
        os.system("pause")
        os.system("cls")
    elif pilihan == 2:
        target_barang = input("Masukkan nama barang yang ingin dicari: ")
        result = sequential(daftar_barang, target_barang)
        if result == -1:
            print(f"Barang {target_barang} tidak ditemukan")
        else:
            print(f"Barang {target_barang} ditemukan di indeks {result}")
        os.system("pause")
        os.system("cls")
    elif pilihan == 3:
        barang_baru = input("Masukkan nama barang yang ingin ditambahkan: ")
        tambah_barang(daftar_barang, barang_baru)
        os.system("pause")
        os.system("cls")
    elif pilihan == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang benar.")