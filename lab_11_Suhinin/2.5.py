try:
    numbers = []

    with open("file1.txt", "r", encoding="utf-8") as file1:
        for line in file1:
            numbers.append(int(line.strip()))

    with open("file2.txt", "r", encoding="utf-8") as file2:
        for line in file2:
            numbers.append(int(line.strip()))

    unique_numbers = sorted(set(numbers))

    with open("merged.txt", "w", encoding="utf-8") as merged:
        for number in unique_numbers:
            merged.write(str(number) + "\n")

    print("Дані успішно об'єднані")

except FileNotFoundError:
    print("Один із файлів не знайдено")

except ValueError:
    print("У файлі містяться некоректні дані")

except PermissionError:
    print("Немає доступу до файлу")

except Exception as error:
    print("Сталася помилка:", error)