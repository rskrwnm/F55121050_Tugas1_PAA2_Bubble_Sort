import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Tampilkan nama
print("|==================================================================================================|")
print("|                                  Reski Dwi Ramadhani Irawan_F55121050                            |")
print("|==================================================================================================|")

# Melakukan input nilai
input_str = input("Masukkan nilai yang ingin diurutkan (pisahkan dengan spasi): ")
arr = list(map(int, input_str.split()))
print("Nilai Awal:", arr)

start_time = time.time()
insertion_sort(arr)
end_time = time.time()

execution_time = end_time - start_time

print("Array Terurut:", arr)
print(f"Waktu Eksekusi: {execution_time} detik")