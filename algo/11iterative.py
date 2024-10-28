def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print("Факториал 5 равен:", factorial_iterative(5))