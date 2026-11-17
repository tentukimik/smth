import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Окно")
root.geometry("350x160")

root.columnconfigure(1, weight=1)

tk.Label(root, text="Имя:").grid(row=0, column=0, padx=10, pady=5)

name = tk.Entry(root)
name.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Группа:").grid(row=1, column=0, padx=10, pady=5)

group = ttk.Combobox(root, values=["Группа 1", "Группа 2", "Группа 3"], state="readonly")
group.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

result = tk.Label(root, text="")
result.grid(row=3, column=0, columnspan=2, pady=5)

def show():
    result.config(text=f"Имя: {name.get()}, группа: {group.get()}")

tk.Button(root, text="Показать", command=show).grid(
    row=2, column=0, columnspan=2, pady=5
)

root.mainloop()
