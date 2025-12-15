import time
def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)
def tail_fib(n, a=0, b=1):
    return a if n == 0 else b if n == 1 else tail_fib(n-1, b, a+b)
n = 35
t1 = time.time()
f1 = fib(n)
t2 = time.time()
print(f"fib({n})={f1}, time: {t2-t1:.6f}s")

t1 = time.time()
f2 = tail_fib(n)
t2 = time.time()
print(f"tail_fib({n})={f2}, time: {t2-t1:.6f}s")
