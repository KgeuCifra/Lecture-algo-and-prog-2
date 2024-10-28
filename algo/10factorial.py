def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Факториал 5 равен:", factorial(5))