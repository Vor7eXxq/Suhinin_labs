def factorial_gen(max_n):
    factorial = 1
    for i in range(max_n + 1):
        if i > 0:
            factorial *= i
        yield factorial
print(list(factorial_gen(5)))