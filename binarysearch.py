import os

# Daftar buku yang sudah diurutkan berdasarkan judul
books = [
    "A Tale of Two Cities",
    "Brave New World",
    "Crime and Punishment",
    "Don Quixote",
    "Frankenstein",
    "Great Expectations",
    "Moby Dick",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "War and Peace"
]

# Fungsi binary search yang mengembalikan daftar indeks dengan substring yang cocok
def binary_search(arr, target):
    results = []
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if target.lower() in guess.lower(): # Memeriksa apakah substring target ada dalam elemen yang ditebak
            # Cari ke kiri dan ke kanan dari mid untuk semua kemungkinan kecocokan
            left = mid
            right = mid
            while left >= low and target.lower() in arr[left].lower(): # Cari ke kiri
                results.append(left)
                left -= 1
            while right <= high and target.lower() in arr[right].lower(): # Cari ke kanan
                if right != mid:  # Hindari duplikasi
                    results.append(right)
                right += 1
            break
        elif guess.lower() > target.lower():
            high = mid - 1
        else:
            low = mid + 1

    return results

# Buku ditemukan berdasarkan judul
def find_books_by_partial_title(title):
    indices = binary_search(books, title)
    if indices:
        return [f"Buku ditemukan: '{books[index]}' pada indeks {index}" for index in indices]
    else:
        return ["Buku tidak ditemukan"]

# Fungsi untuk menampilkan buku
def display_books():
    for index, book in enumerate(books):
        print(f"{book}")

# Fungsi untuk menambah buku
def add_book(title):
    books.append(title)
    books.sort()

def menu():
    while True:
        print("======================================")
        print("PROGRAM PENCARIAN BUKU (BINARY SEARCH)")
        print("======================================\n")
        print("1. Tampilkan Buku")
        print("2. Cari Buku")
        print("3. Tambah Buku")
        print("4. Keluar")

        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            display_books()
            os.system("pause")
            os.system("cls")
        elif choice == '2':
            user_input = input("Masukkan judul atau bagian dari judul buku yang dicari: ")
            results = find_books_by_partial_title(user_input)
            for result in results:
                print(result)
            os.system("pause")
            os.system("cls")
        elif choice == '3':
            new_book = input("Masukkan judul buku yang ingin ditambahkan: ")
            add_book(new_book)
            print(f"Buku '{new_book}' berhasil ditambahkan.")
            os.system("pause")
            os.system("cls")
        elif choice == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

menu()