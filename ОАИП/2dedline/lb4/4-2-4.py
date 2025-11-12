import random
t = [random.randint(10, 25) for _ in range(14)]
print(f"Темпы: {t}")
print(f"Макс: {max(t)}°C")
print(f"Мин: {min(t)}°C")
avg = sum(t) / len(t)
print(f"Средняя: {avg:.1f}°C")
above = sum(1 for x in t if x > avg)
print(f"Выше средней: {above} дней")
print(f"По порядку: {sorted(t)}")
f = [x * 9/5 + 32 for x in t]
print(f"Фаренгейты: {f}")
