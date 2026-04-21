def count_digits(n):
    if n <10:
        return n
    else:
        return 1 +count_digits(n//10)
print(count_digits(123))