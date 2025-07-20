import random
import time

#insertion Sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
# bubble Sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        doi = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                # đổi
                arr[j], arr[j+1] = arr[j+1], arr[j]
                doi = True
        if doi == False:
            break
    return arr

# test
kich_thuoc = [100, 500, 1000]

for size in kich_thuoc:
    print("mẩng", size, "phân tử ")
    data1 = random.sample(range(10000), size)
    data2 = data1.copy()
    #insertion sort
    start = time.time()
    insertion_sort(data1)
    end = time.time()
    print("time insertion sort:", end - start, "giây")
    # bubble sort
    start = time.time()
    bubble_sort(data2)
    end = time.time()
    print("time bubble sort:   ", end - start, "giây")
    print()
