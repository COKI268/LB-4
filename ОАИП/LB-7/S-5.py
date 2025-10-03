
kal = input("введите числа вот так через пробел (число знак число)").split()
a = float(kal[0])
s = kal[1]
b = float(kal[2])
if s == '+':
    r = a + b
elif s == '-':
    r = a - b
elif s == '*':
    r = a * b
elif s == '/':
    r = a / b
elif s == '%':
    r = a % b
elif s == '//':
    r = a // b
elif s == '**':
    r = a ** b
elif s == '%%':
    r = (b / 100) * a
elif s == '/**':
    r = math.sqrt(a)
else:
    r = ("Неизвестная операция")

print("вывод",r)
