def replace_text():
    text = input("Введите произвольный текст: ")
    
    replacement = input("Введите две строки через пробел (строка1 строка2): ")
    
    parts = replacement.split()
    
    if len(parts) < 2:
        print("Ошибка: нужно ввести две строки через пробел")
        return
    
    old_str = parts[0]
    new_str = parts[1]
    
    formatted_text = text.replace(old_str, new_str)
    
    print("Отформатированный текст:")
    print(formatted_text)

if __name__ == "__main__":
    replace_text()
