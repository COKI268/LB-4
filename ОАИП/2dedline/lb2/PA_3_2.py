text = input("Введите текст: ")
l = d = p = s = 0
for char in text:
    if char.isalpha():
        l += 1
    elif char.isdigit():
        d += 1
    elif char in '.,!?:;':
        p += 1
    elif char == ' ':
        s += 1
print(f"букв = {l}")
print(f"цифр = {d}")
print(f"знаков препинания = {p}")
print(f"пробелов = {s}")
