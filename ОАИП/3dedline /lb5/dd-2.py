class BankAccount:
    def __init__(self, name, b=0):
        self.name = name
        self.b = b
    
    def deposit(self, a):
        self.b += a
    
    def withdraw(self, a):
        if a > self.b:
            print("Недостаточно средств!")
        else:
            self.b -= a
    
    def get_balance(self):
        return self.b

a = BankAccount("Ivanov", 100)
a.deposit(50)
a.withdraw(200)
a.withdraw(30)
print(a.get_balance())
