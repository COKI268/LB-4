fio = input("введите ФИО через пробел")
a= fio.split()
f = a[0]
i = a[1]
o = a[2]
f = f[0].upper() + f[1:].lower()
i = i[0].upper() + i[1:].lower()
o = o[0].upper() + o[1:].lower()

print("Добро пожаловать", f, i, o)
