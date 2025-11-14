def format_report(report_title, *data, **properties):
    """
    Печатает красивый отчет
    """
    print(f"--- Отчет: {report_title} ---")
    print("Данные:")
    for item in data:
        print(f" - {item}")
    
    print("Свойства:")
    for key, value in properties.items():
        print(f" - {key}: {value}")
    print("------------------------------")

format_report(
    "Мой отчет",
    "Все хорошо",
    "Работает",
    author="Я",
    date="сегодня"
)
