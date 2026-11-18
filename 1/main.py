import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Окно")
root.geometry("350x160")

tk.Label(root, text="Имя:").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Группа:").pack()
group = ttk.Combobox(root, values=["Группа 1", "Группа 2", "Группа 3"])
group.pack()

def show():
    username = name.get().strip()

    if not username:
        messagebox.showwarning("Ошибка", "Введите имя")
        return

    card = tk.Toplevel(root)
    card.title("Карточка")

    tk.Label(card, text=f"Имя: {username}").pack()
    tk.Label(card, text=f"Группа: {group.get()}").pack()
    tk.Button(card, text="Закрыть", command=card.destroy).pack()
    card.bind("<Escape>", lambda e: card.destroy())

def clear():
    name.delete(0, tk.END)
    group.set("")

tk.Button(root, text="Показать", command=show).pack()
tk.Button(root, text="Очистить", command=clear).pack()

root.mainloop()