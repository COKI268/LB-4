import time, random

def find_duplicates(arr):
    dup = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                dup.append(arr[i])
    return dup

arr1 = [random.randint(1,1000) for _ in range(5000)]
start = time.time()
find_duplicates(arr1)
t1 = time.time() - start

arr2 = [random.randint(1,1000) for _ in range(10000)]
start = time.time()
find_duplicates(arr2)
t2 = time.time() - start

print(f"5000: {t1:.1f}s, 10000: {t2:.1f}s")
print(f"Выросло в {t2/t1:.1f} раза (должно в ~4)")
