date = input()
if len(date) != 10 or date[2] != '.' or date[5] != '.':
    print("Ошибка")
else:
    try:
        d, m, y = int(date[:2]), int(date[3:5]), int(date[6:])
        if not (1900 <= y <= 2025 and 1 <= m <= 12):
            print("Ошибка")
        elif m in [1,3,5,7,8,10,12]:
            print("Корректно" if 1 <= d <= 31 else "Ошибка")
        elif m in [4,6,9,11]:
            print("Корректно" if 1 <= d <= 30 else "Ошибка")
        else:
            leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
            print("Корректно" if 1 <= d <= (29 if leap else 28) else "Ошибка")
    except:
        print("Ошибка")
