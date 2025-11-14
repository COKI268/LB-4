num = int(input("введите число: "))
a = 0
while num > 0:
    a += num % 10
    num = num // 10
print (f"Сумма чисел {a}")
