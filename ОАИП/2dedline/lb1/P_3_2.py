a = input("введите текст: ").lower().replace(' ',' ')
b , c = 0 , len(a)-1
while b < c:
    if a[b] != a[c]:
        print('нет')
        break
    b += 1
    c -= 1
else:
    print('да')
