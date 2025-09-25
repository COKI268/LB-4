import random
import string

def generate_random_string(length: int) -> str:
    """Генерирует случайную строку из букв ASCII и цифр."""

    characters = string.ascii_letters + string.digits + string.punctuation + ' '
  
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

message = input("Введите сообщение для кодирования: ")


n = int(input("Введите количество подстановочных символов (n): "))


encoded_message_parts = []

for char in message:

    encoded_message_parts.append(char)

    random_chars = generate_random_string(n)
    encoded_message_parts.append(random_chars)

encoded_message = ''.join(encoded_message_parts)

print("\n" + "="*50)
print("КОДИРОВАННОЕ ПОСЛАНИЕ")
print("="*50)
print(encoded_message)
