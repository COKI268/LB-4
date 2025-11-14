def build_user_profile(user_id, **kwargs):
    """
    Создает словарь с информацией о пользователе
    """
    result = {'user_id': user_id}
    for key, value in kwargs.items():
        result[key] = value
    return result

profile = build_user_profile(101, name="Анна", status="online")
print(profile) 
