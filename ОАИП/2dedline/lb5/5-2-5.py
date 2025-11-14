math = {"Alice", "Bob", "Charlie", "David"}
physics = {"Bob", "David", "Eve", "Frank"}
cs = {"Alice", "Charlie", "Eve", "Grace"}

all_three = math & physics & cs
only_one = (math - physics - cs) | (physics - math - cs) | (cs - math - physics)
math_not_physics = math - physics
all_students = math | physics | cs

print(f"Все три курса: {all_three}")
print(f"Только один курс: {only_one}")
print(f"Математика но не физика: {math_not_physics}")
print(f"Всего студентов: {len(all_students)}")
