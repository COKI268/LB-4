class Multiplier:
    def __init__(self, m):
        self.m = m
    
    def __call__(self, n):
        return self.m * n

by_5 = Multiplier(5)
print(by_5(10))
print(by_5(2))
