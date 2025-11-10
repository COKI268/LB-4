contacts = {
    "Иван": "+79123456789",
    "Мария": "+79234567890", 
    "Петр": "+79345678901"
}

while True:
    print("\nТелефонная книга")
    print("1 - Контакты")
    print("2 - Добавить")
    print("3 - Удалить") 
    print("4 - Выход")
    
    cmd = input("Выбор: ")
    
    if cmd == "1":
        if contacts:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Пусто")
    
    elif cmd == "2":
        name = input("Имя: ").strip()
        if name in contacts:
            print("Уже есть")
        else:
            phone = input("Телефон: ").strip()
            contacts[name] = phone
            print("Добавлен")
    
    elif cmd == "3":
        name = input("Имя для удаления: ").strip()
        if name in contacts:
            del contacts[name]
            print("Удален")
        else:
            print("Нет такого")
    
    elif cmd == "4":
        print("Пока!")
        break
    
    else:
        print("Неверно")
