text = input("Введите строку: ")
b = "аеёиоуыэюяaeiouyAEIOUYАЕЁИОУЫЭЮЯ"
r = ""
a = 0
while a < len(text):
    c = text[a]
    if c not in b:
        r +=c
    a +=1
print(r)
