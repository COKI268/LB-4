import random

num = [random.randint(1, 100) for _ in range(10)]
a = [x for x in num if x % 2 == 0]
b = [x for x in num if x > 50]

print(f"Исходный: {num}")
print(f"Четные: {a}")
print(f"Больше 50: {b}")
