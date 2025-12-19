class Student:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    
    def is_excellent(self):
        if self.s == 5:
            return True
        return False

s1 = Student("Vasya", 4.5)
s2 = Student("Petya", 5)

print(s1.is_excellent())
print(s2.is_excellent())
