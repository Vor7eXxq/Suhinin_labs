import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    """Функція для розрахунку температури"""
    try:

        celsius = float(entry_celsius.get())


        fahrenheit = celsius * 9 / 5 + 32


        label_result.config(text=f"Результат: {fahrenheit:.1f} °F", fg="green")

    except ValueError:

        messagebox.showerror("Помилка", "Будь ласка, введіть коректне число!")
        label_result.config(text="Помилка введення!", fg="red")


root = tk.Tk()
root.title("Конвертер температури")
root.geometry("400x250")
root.configure(pady=20)


label_info = tk.Label(root, text="Введіть температуру в °C:", font=("Arial", 12))
label_info.pack(pady=5)

entry_celsius = tk.Entry(root, font=("Arial", 12), width=15, justify="center")
entry_celsius.pack(pady=5)
entry_celsius.insert(0, "0")


button_convert = tk.Button(
    root,
    text="Конвертувати",
    font=("Arial", 11, "bold"),
    command=convert_temperature,
    bg="#4CAF50",
    fg="white"
)
button_convert.pack(pady=15)


label_result = tk.Label(root, text="Результат: 32.0 °F", font=("Arial", 14, "bold"))
label_result.pack(pady=10)

root.mainloop()