def text_with_step():
    
    text = input("Введите произвольный текст: ")
    
    try:
        step = int(input("Введите шаг: "))
    except ValueError:
        print("Ошибка: шаг должен быть целым числом")
        return
    
    result = text[::step]
    print(f"Текст с шагом {step}:")
    print(result)

if __name__ == "__main__":
    text_with_step()
