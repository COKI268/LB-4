def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
class SequenceAnalyzer:
    def get_evens(self, gen):
        return [num for num in gen if num % 2 == 0]
fib = fibonacci_gen(10)
analyzer = SequenceAnalyzer()
result = analyzer.get_evens(fib)
print(result)  
