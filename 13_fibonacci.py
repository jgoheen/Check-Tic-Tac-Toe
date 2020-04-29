

def fibonacci(n):
    result = []
    a = 0
    b = 1
    i = 0
    while i < n:
        result.append(a)
        a, b = b, a + b
        i = i + 1
    print(result)

fib = input("How many Fibonacci number to print? ")
fib = int(fib)

fibonacci(fib)