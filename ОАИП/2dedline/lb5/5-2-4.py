text = input("Введите текст: ")
words = set(text.lower().split())

print(f"Уникальных слов: {len(words)}")
print(f"Длинные: {[w for w in words if len(w) > 5]}")
print(f"Есть python/programming: {any(w in words for w in ['python','programming'])}")
