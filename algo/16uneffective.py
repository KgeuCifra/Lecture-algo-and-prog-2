
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print("10-е число Фибоначчи:", fib(10))