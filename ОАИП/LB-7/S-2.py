print("РЕГИСТРАЦИЯ")
passwd = input("Придумайте пароль")
Ppassword = input("Подтвердите пароль:")
if passwd == Ppassword:
    print("Пароль успешно установлен")
else:
    print("Пароли не совпадают")
    exit()
print("АВТОРИЗАЦИЯ")
Lpasswd = input("Введите пароль для входа")
if Lpasswd == passwd:
    print("Access")
else:
    print("Denied")
