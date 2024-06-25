def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # jika elemen berada di tengah
        if arr[mid] < x:
            low = mid + 1
        # jika elemen berada di sebelah kiri
        elif arr[mid] > x:
            high = mid - 1
        # elemen ditemukan
        else:
            return mid
    return -1

def main():
    # Menerima input daftar elemen (pisahkan dengan spasi)
    arr = list(map(int, input("Masukkan elemen yang sudah terurut: ").split()))
    x = int(input("Masukkan Elemen Yang Dicari: "))
    
    # Menerima input elemen yang dicari
    result = binary_search(arr, x)
    
    if result != -1:
        print(f"Elemen ditemukan pada index {result}")
    else:
        print("Elemen tidak ditemukan")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()