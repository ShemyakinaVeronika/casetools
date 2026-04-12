"""
Программа для решения квадратных уравнений.

Позволяет вводить коэффициенты a, b и c,
вычислять корни уравнения и отображать результат
в графическом интерфейсе.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt


def quadratic_equation(a, b, c):
    """
    Вычисляет корни квадратного уравнения.

    Уравнение имеет вид: a*x^2 + b*x + c = 0.

    Параметры:
        a — коэффициент при x^2
        b — коэффициент при x
        c — свободный член

    Возвращает:
        list: список корней уравнения (один или два корня),
        либо строку с сообщением об ошибке:
        - если a = 0 — уравнение не является квадратным
        - если дискриминант < 0 — действительных корней нет
    """

    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return "Неверный тип коэффициентов."

    if a == 0:
        return "Это не квадратное уравнение."

    d = b**2 - 4 * a * c

    if d < 0:
        return "Действительных корней нет."

    if d == 0:
        return [round(-b / (2 * a), 3)]

    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    return sorted([round(x1, 3), round(x2, 3)])


def solve():
    """
    Обрабатывает нажатие кнопки «Решить».

    Получает значения коэффициентов из полей ввода,
    вызывает функцию вычисления корней и отображает результат
    в интерфейсе пользователя.

    В случае ошибки ввода выводит сообщение об ошибке.
    """
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        result = quadratic_equation(a, b, c)
        result_label.config(text=f"Результат: {result}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")


def clear():
    """
    Очищает поля ввода и результат.

    Удаляет введённые значения коэффициентов и
    сбрасывает отображаемый результат,
    позволяя пользователю начать ввод заново.
    """
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    result_label.config(text="Результат:")


# Создаем графический интерфейс (GUI)
# Создаем главное окно приложения
root = tk.Tk()
root.title("Решение квадратного уравнения")
root.geometry("420x320")
root.configure(bg="#1e1e2f")

# Настраиваем стиль виджетов
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 11), padding=6)
style.configure("TEntry", padding=5)

# Настраиваем заголовок
title = tk.Label(
    root,
    text="ax² + bx + c = 0",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#1e1e2f",
)
title.pack(pady=15)  # Отступы

# Создаем фрейм - контейнер для группировки виджетов
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

# Создаем поля ввода
tk.Label(frame, text="a:", font=("Segoe UI", 12), fg="white", bg="#1e1e2f").grid(
    row=0, column=0, padx=5, pady=5
)

entry_a = ttk.Entry(frame, width=15)
entry_a.grid(row=0, column=1)

tk.Label(frame, text="b:", font=("Segoe UI", 12), fg="white", bg="#1e1e2f").grid(
    row=1, column=0, padx=5, pady=5
)

entry_b = ttk.Entry(frame, width=15)
entry_b.grid(row=1, column=1)

tk.Label(frame, text="c:", font=("Segoe UI", 12), fg="white", bg="#1e1e2f").grid(
    row=2, column=0, padx=5, pady=5
)

entry_c = ttk.Entry(frame, width=15)
entry_c.grid(row=2, column=1)

# Создаем кнопки
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=15)

solve_btn = ttk.Button(btn_frame, text="Решить", command=solve)
solve_btn.grid(row=0, column=0, padx=10)

clear_btn = ttk.Button(btn_frame, text="Очистить", command=clear)
clear_btn.grid(row=0, column=1, padx=10)

# Создаем метку для вывода результата
result_label = tk.Label(
    root, text="Результат:", font=("Segoe UI", 12), fg="#4CAF50", bg="#1e1e2f"
)
result_label.pack(pady=10)

# Запускаем главный цикл приложения
root.mainloop()
