import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Iterasi {i+1}:")
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(arr)

        if not swapped:
            break

    return arr

# Tampilkan nama
print("|==================================================================================================|")
print("|                                  Reski Dwi Ramadhani Irawan_F55121050                            |")
print("|==================================================================================================|")


# Melakukan input nilai
input_str = input("Masukkan nilai yang ingin diurutkan (pisahkan dengan spasi): ")
arr = list(map(int, input_str.split()))
print("Nilai Awal:", arr)

start_time = time.time()
sorted_arr = bubble_sort(arr)
end_time = time.time()

execution_time = end_time - start_time

print("Array Terurut:", sorted_arr)
print(f"Waktu Eksekusi: {execution_time} detik")