FILE_NAME = "passwords.txt"

def encrypt(text):
    encrypted = ""

    for char in text:
        encrypted += chr(ord(char) + 1)

    return encrypted

def decrypt(text):
    decrypted = ""

    for char in text:
        decrypted += chr(ord(char) - 1)

    return decrypted

def add_record(site, password):
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            encrypted_password = encrypt(password)
            file.write(f"{site}:{encrypted_password}\n")

        print(f"Додано запис для {site}")

    except PermissionError:
        print("Помилка доступу до файлу")

    except Exception as error:
        print("Помилка:", error)

def find_password(site):
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:

            for line in file:
                line = line.strip()

                if ":" not in line:
                    print("Невірний формат даних")
                    continue

                saved_site, encrypted_password = line.split(":", 1)

                if saved_site == site:
                    password = decrypt(encrypted_password)
                    print(f"Пароль для {site}: {password}")
                    return

            print("Сайт не знайдено")

    except FileNotFoundError:
        print("Файл не існує")

    except PermissionError:
        print("Помилка доступу до файлу")

    except Exception as error:
        print("Помилка:", error)

def delete_record(site):
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        found = False

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for line in lines:
                if ":" not in line:
                    continue

                saved_site, _ = line.strip().split(":", 1)

                if saved_site != site:
                    file.write(line)
                else:
                    found = True

        if found:
            print(f"Запис для {site} видалено")
        else:
            print("Сайт не знайдено")

    except FileNotFoundError:
        print("Файл не існує")

    except PermissionError:
        print("Помилка доступу до файлу")

    except Exception as error:
        print("Помилка:", error)

add_record("google.com", "myPass123")
add_record("github.com", "dev2024")

find_password("google.com")