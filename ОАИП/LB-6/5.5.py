def word_search():
    text = input("Введите произвольный текст: ")
    
    search_word = input("Введите слово для поиска: ")
    
    words = text.split()
    
    count = words.count(search_word)
    
    first_index = -1
    for i, word in enumerate(words):
        if word == search_word:
            first_index = i
            break
    
    text_without_word = text.replace(search_word, "")
    
    print(f"Количество вхождений слова '{search_word}': {count}")
    
    if first_index != -1:
        print(f"Индекс первого вхождения: {first_index}")
    else:
        print("Слово не найдено")
    
    print("Текст без искомого слова:")
    print(text_without_word)

if __name__ == "__main__":
    word_search()
