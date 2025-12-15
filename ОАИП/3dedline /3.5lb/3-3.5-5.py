import sys

def create_list(n):
    return [i**2 for i in range(n)]

def create_gen(n):
    return (i**2 for i in range(n))

n = 1000000
lst = create_list(n)
gen = create_gen(n)

print(f"Список: {sys.getsizeof(lst)} байт")
print(f"Генератор: {sys.getsizeof(gen)} байт")

print("Первые 3 из списка:", lst[:3])
print("Первые 3 из генератора:", [next(gen) for _ in range(3)])
