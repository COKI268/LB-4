def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(is_palindrome("топот"))
print(is_palindrome("python"))
print(is_palindrome("Топот"))
