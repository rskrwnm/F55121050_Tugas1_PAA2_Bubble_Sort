# Reski Dwi Ramadhani Irawan
# F55121050
import time

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = []
l = int(input("Masukkan panjang array: "))
for i in range(l):
    k = int(input("Nilai array: "))
    arr.append(k)

print("Array:", arr)
start_time = time.time()
bubbleSort(arr)
end_time = time.time()

print("\nSorted Array is:")
for i in range(len(arr)):
    print(arr[i])

print("Execution time: %.5f seconds" % (end_time - start_time))