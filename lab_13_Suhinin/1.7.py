text = ["Apple", "banana", "Apricot", "blueberry", "avocado"]
letter = input("Введіть букву на яку повинно починатись слово: ")
filtered = [i for i in text if i[0] == letter.lower() or i[0] == letter.upper()]
print(filtered)
