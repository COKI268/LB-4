import time, random

def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        need = target - num
        if need in seen:
            return (need, num)
        seen.add(num)
    return None

arr = [random.randint(1,10000) for _ in range(10000)]
target = random.randint(10000,20000)

start = time.time()
find_pair_slow(arr, target)
t_slow = time.time() - start

start = time.time()
find_pair_fast(arr, target)
t_fast = time.time() - start

print(f"Медленно: {t_slow:.2f}s, Быстро: {t_fast:.5f}s")
print(f"Быстрее в {t_slow/t_fast:.0f} раз")
