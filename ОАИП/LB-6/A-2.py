text = input("введите текст")
f = input("введите что заменить и на что через пробел")
s = f.split()
str1 = s[0]
str2 = s[1]
Rtext = text.replace(str1,str2)
print("результат")
print(Rtext)
