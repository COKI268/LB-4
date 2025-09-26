def substring_extraction():
    
    text = input("Введите произвольный текст: ")
    
    range_input = input("Введите диапазон через пробел (начало конец): ")
    
    try:
        parts = range_input.split()
        
        if len(parts) < 2:
            print("Ошибка: нужно ввести два числа через пробел")
            return
        
        start = int(parts[0]) - 1  
        end = int(parts[1])       
        
        if start < 0 or end > len(text) or start >= end:
            print("Ошибка: некорректный диапазон")
            return
        
        substring = text[start:end]
        
        print(f"Подстрока с {start + 1} по {end} символ:")
        print(substring)
        
    except ValueError:
        print("Ошибка: введите целые числа")

if __name__ == "__main__":
    substring_extraction()
