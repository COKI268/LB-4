text = input("Введите текст")
word = input("Введите слово для поиска")
if word in text:
    с = text.count(word)
    print(f"Слово '{word}' найдено в тексте")
    print(f"Количество: '{с}' ")
else:
    print(f"Слова '{word}' нет в тексте")
    
