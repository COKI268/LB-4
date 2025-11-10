text = input("Введите произвольную строку: ")
c = {}
for z in text.lower():
    if z in c:
        c[z] += 1
    else:
        c[z] = 1
print("Результат подсчета символов:")
print(c)
