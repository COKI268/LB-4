import string
stats = {}
print("Введите текст (пустая строка - конец):")
while True:
    text = input()
    if not text:
        break

    for word in text.split():
        clean = word.strip(string.punctuation).lower()
        if clean:
            stats[clean] = stats.get(clean, 0) + 1
print("\nСтатистика:")
print(stats)
