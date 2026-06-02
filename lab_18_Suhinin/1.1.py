import tkinter as tk

def close_program():
    """Функція для закриття програми"""
    root.destroy()
root = tk.Tk()
root.title("Моя вітальна картка")
root.geometry("400x300")
root.configure(pady=20)
label_title = tk.Label(root, text="Вітаю!", font=("Arial", 18, "bold"))
label_title.pack(pady=10)
label_name = tk.Label(root, text="Сухінін Богдан", font=("Arial", 14))
label_name.pack(pady=5)
label_group = tk.Label(root, text="Група: КН 1/1", font=("Arial", 12, "italic"))
label_group.pack(pady=5)
button_close = tk.Button(root, text="Закрити", font=("Arial", 11), command=close_program, width=10)
button_close.pack(pady=30)
root.mainloop()