def calc_avg(numbers):
    """
    Находит среднее арифметическое чисел в списке
    
    Args:
        numbers: список чисел
        
    Returns:
        среднее значение
    """
    if len(numbers) == 0:
        return 0.0
    return sum(numbers) / len(numbers)

print(calc_avg([10, 20, 30, 40]))  


def fmt_fio(parts, capitalize=True):
    """
    Собирает ФИО из частей
    
    Args:
        parts: список с фамилией, именем, отчеством
        capitalize: делать ли заглавные буквы
        
    Returns:
        строка с ФИО
    """
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
    return fio

print(fmt_fio(["петров", "иван", "сергеевич"]))  


def filter_scores(data_dict, min_value):
    """
    Оставляет только оценки выше минимальной
    
    Args:
        data_dict: словарь с оценками
        min_value: минимальная оценка
        
    Returns:
        отфильтрованный словарь
    """
    result = {}
    for subject, score in data_dict.items():
        if score >= min_value:
            result[subject] = score
    return result

scores = {"math": 95, "history": 78, "english": 88}
print(filter_scores(scores, 90))
