n = int(input("Сколько чисел вы хотите ввести? "))
num = []
for i in range(n):
    num2 = int(input(f"Введите число {i+1}: "))
    num.append(num2)
maxi = max(num)
mini = min(num)
ave = sum(num) / n
count_a = sum(1 for x in num if x > ave)
print("Результаты:")
print(f"Максимальное: {maxi}")
print(f"Минимальное: {mini}")
print(f"Среднее: {ave}")
print(f"Чисел больше среднего: {count_a}")
