class Task:
    def __init__(self, d, p):
        self.d = d
        self.p = p

class TaskManager:
    def __init__(self):
        self.list_t = []
    
    def add_task(self, d, p):
        t = Task(d, p)
        self.list_t.append(t)
    
    def show_tasks(self):
        for t in self.list_t:
            print(f"{t.d} - {t.p}")

m = TaskManager()
m.add_task("Купить хлеб", 1)
m.add_task("Сделать домашку", 10)
m.show_tasks()
