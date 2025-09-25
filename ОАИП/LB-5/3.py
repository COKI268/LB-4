
fio = input("Введите ФИО через пробел: ")

components = fio.split()

if len(components) == 3:
    surname, name, patronymic = components
    
    print("\nРезультат:")
    print("Фамилия:".ljust(10), surname.upper())
    print("Имя:".ljust(10), name.upper())
    print("Отчество:".ljust(10), patronymic.upper())
else:
    print("Неверный формат! Пример: Иванов Пётр Сергеевич")
