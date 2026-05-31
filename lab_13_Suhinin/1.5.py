nums = ["0501234567", "+380501234567", "(050)123-45-67"]
corrected = [
    "+380" + ''.join(filter(str.isdigit, number))[-10:]
    for number in nums
]
print(corrected)