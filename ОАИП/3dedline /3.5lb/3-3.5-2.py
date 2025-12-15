import time

lst = list(range(100000))

start = time.time()
for _ in range(1000):
    lst.pop(0)
t1 = time.time() - start

lst = list(range(100000))
start = time.time()
for _ in range(1000):
    lst.pop()
t2 = time.time() - start

print(f"pop(0): {t1:.3f}s, pop(): {t2:.3f}s")
print(f"pop() быстрее в {t1/t2:.0f} раз")
