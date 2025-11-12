tasks = []
while True:
    print("\n1-показать 2-добавить 3-удалить 4-Exit")
    c = input("> ")
    
    if c == "1":
        for i,t in enumerate(tasks,1):
            print(f"{i}.{t}")
    elif c == "2":
        tasks.append(input("Task: "))
    elif c == "3":
        n = int(input("Num: "))-1
        if 0 <= n < len(tasks):
            tasks.pop(n)
    elif c == "4":
        break
