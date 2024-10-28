fib_cache = {}

def fib_dp(n):
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        fib_cache[n] = n
    else:
        fib_cache[n] = fib_dp(n-1) + fib_dp(n-2)
    return fib_cache[n]
print("10-е число Фибоначчи:", fib_dp(10))