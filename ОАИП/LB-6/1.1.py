
def format_fio():
    
    full_name = input("Введите ваше ФИО через пробел: ")
    

    parts = full_name.split()
    
    
    formatted_parts = [part.capitalize() for part in parts]
    

    formatted_name = ' '.join(formatted_parts)

    print(f"Добро пожаловать {formatted_name}")
    
if __name__ == "__main__":
    format_fio()
