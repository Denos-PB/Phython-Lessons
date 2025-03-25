import math

def calculate_triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Сторони трикутника повинні бути додатними числами")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Неможливо створити трикутник з заданими сторонами")

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area

if __name__ == "__main__":
    try:
        side_a = float(input("Введіть довжину першої сторони трикутника: "))
        side_b = float(input("Введіть довжину другої сторони трикутника: "))
        side_c = float(input("Введіть довжину третьої сторони трикутника: "))

        area = calculate_triangle_area(side_a, side_b, side_c)
        print(f"Площа трикутника зі сторонами {side_a}, {side_b}, {side_c} дорівнює {area:.4f}")

    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")