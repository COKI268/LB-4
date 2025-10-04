a, b, c =(map(int, input("Введите переменные ").split()))
print("a * b =", a*b)
print("b * c =", b*c)
print("c * a =", c*a)
d = a*b
e = b*c
f = c*a
print("Первое число в 4 степени равно", pow(a, 4))
print("Остаток ", b % c)
print("Целочисленное деление ", c//d)
r = pow(a, 4)
t= b % c
y= c//d
print("Сложение чисел", r+t+y)
