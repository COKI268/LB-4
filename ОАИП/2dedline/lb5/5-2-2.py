students = [("Анна",21,4.5),("Петр",22,4.2),("Мария",19,4.8),("Иван",20,4.1),("Елена",23,4.6)]

print("Старше 20 лет:")
for n,a,s in students:
    if a>20: print(f"- {n} ({a}), балл: {s}")

best = max(students, key=lambda x:x[2])
print(f"\nЛучший: {best[0]}, балл: {best[2]}")

print("\nПо имени:")
for n,a,s in sorted(students):
    print(f"- {n}: {a} лет, балл: {s}")
