def squares_generator(n):
    """Функция-генератор, возвращающая квадраты чисел от 1 до n"""
    for i in range(1, n + 1):
        yield i **2
gen = squares_generator(4)
for val in gen:
    print(val)
