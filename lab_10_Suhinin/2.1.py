def flexible_average(*args):
    numbers = [x for x in args if isinstance(x, (int, float))]
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
print(flexible_average(1,'a',3))