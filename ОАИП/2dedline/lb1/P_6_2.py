s = input("Символ: ")
h = int(input("Высота: "))
w = int(input("Ширина: "))
r = 0
while r < h:
    l = ""
    c = 0
    while c < w:
        l += s
        c += 1
    print(l)
    r += 1
