class Hero:
    def __init__(self, n, h=100, a=20):
        self.n = n
        self.h = h
        self.a = a
    
    def strike(self, t):
        t.h -= self.a

k = Hero("Arthur", 100, 20)
r = Hero("Robin", 80, 15)

k.strike(r)
r.strike(k)

print(f"{k.n}: {k.h}")
print(f"{r.n}: {r.h}")
