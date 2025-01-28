import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox

def draw_koch_segment(t, length, level):
    """Функція для малювання одного сегмента сніжинки Коха."""
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)

def draw_koch_snowflake(t, length, level):
    """Функція для малювання повної сніжинки Коха."""
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    # Створюємо головне вікно для tkinter
    root = tk.Tk()
    root.withdraw()  # Приховуємо основне вікно tkinter

    # Запитуємо рівень рекурсії через діалогове вікно
    while True:
        level = simpledialog.askinteger("Введіть рівень рекурсії", 
                                        "Вкажіть рівень рекурсії для сніжинки Коха (рекомендується 0-5):",
                                        minvalue=0)
        if level is None:  # Якщо користувач закрив вікно
            root.destroy()
            return
        elif 0 <= level <= 5:  # Якщо рівень у межах рекомендації
            break
        else:
            # Повідомляємо, що рівень виходить за межі
            messagebox.showerror("Помилка", "Будь ласка, введіть рівень від 0 до 5!")

    # Налаштування вікна Turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")

    # Налаштування Turtle
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(-200, 100)  # Початкове положення
    t.pendown()

    # Малювання сніжинки
    draw_koch_snowflake(t, 400, level)

    # Завершення роботи
    t.hideturtle()

    # Закриваємо tkinter після закриття вікна Turtle
    def close_program():
        root.destroy()  # Закриває tkinter
        turtle.bye()  # Закриває вікно малювання

    # Використовуємо обробник події закриття
    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", close_program)
    screen.mainloop()

if __name__ == "__main__":
    main()
