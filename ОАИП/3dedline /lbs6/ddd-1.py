class Book:
    def __init__(self, t, a, y):
        self.t = t
        self.a = a
        self.y = y
    
    def __str__(self):
        return f'"{self.t}" ({self.a}, {self.y})'
    
    def __repr__(self):
        return f"Book('{self.t}', '{self.a}', {self.y})"

b = Book("1984", "George Orwell", 1949)
print(b)
print(repr(b))
