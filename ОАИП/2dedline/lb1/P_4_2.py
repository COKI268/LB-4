from random import randint

random_num = randint(1, 100)
while True:
    user = int(input("Введите ваше предположение: "))

    if user == random_num:
        print("Угадал")
        break  
    elif user > random_num:
        print("Меньше")
    else:
        print("Больше")
