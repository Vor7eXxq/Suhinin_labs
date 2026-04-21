def reverse_numbers(n,rev = 0):
    if n == 0:
        return rev
    return reverse_numbers(n//10,rev * 10 + n %10)
print(reverse_numbers(123))
