import math


def display_menu():
    print("\n" + "=" * 50)
    print("ГОЛОВНЕ МЕНЮ".center(50))
    print("=" * 50)
    print("1. Координати точки (2D, 3D)")
    print("2. Обчислення математичних виразів")
    print("3. Периметр трикутника")
    print("4. Робота з колом")
    print("5. Рівняння лінії")
    print("6. Функції модуля math")
    print("7. Персональне вітання")
    print("8. Вихід")
    print("=" * 50)


def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Помилка! Введіть коректне число.")


def get_valid_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Значення повинно бути не менше {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Значення повинно бути не більше {max_value}.")
                continue
            return value
        except ValueError:
            print("Помилка! Введіть коректне ціле число.")


# КРОК 2: Робота з координатами
def input_coordinates():
    dim = get_valid_int_input("Введіть розмірність (2 для 2D, 3 для 3D): ", 2, 3)

    x = get_valid_float_input("Введіть координату x: ")
    y = get_valid_float_input("Введіть координату y: ")

    if dim == 3:
        z = get_valid_float_input("Введіть координату z: ")
        return (x, y, z)
    else:
        return (x, y)


def display_coordinates(coords):
    if len(coords) == 2:
        print(f"\nКоординати 2D точки: ({coords[0]:.2f}, {coords[1]:.2f})")
    else:
        print(f"\nКоординати 3D точки: ({coords[0]:.2f}, {coords[1]:.2f}, {coords[2]:.2f})")


def manage_coordinates():
    print("\n--- Робота з координатами точок ---")
    coords = input_coordinates()
    display_coordinates(coords)
    input("\nНатисніть Enter для повернення в меню...")


# КРОК 3: Обчислення математичних виразів
def calculate_expressions():
    print("\n--- Обчислення математичних виразів ---")
    a = get_valid_float_input("Введіть значення a: ")
    b = get_valid_float_input("Введіть значення b: ")

    try:
        expr1 = math.log(a ** 2 + b ** 2)

        expr2 = math.sin((a + b) ** (1 / 7))

        expr3 = math.cos(a ** 12 + b ** 12) ** 3

        print(f"\nРезультати обчислень:")
        print(f"1. ln(a² + b²) = ln({a}² + {b}²) = {expr1:.4f}")
        print(f"2. sin((a + b)^(1/7)) = sin(({a} + {b})^(1/7)) = {expr2:.4f}")
        print(f"3. cos³(a¹² + b¹²) = cos³({a}¹² + {b}¹²) = {expr3:.4f}")
    except ValueError as e:
        print(f"Помилка обчислення: {e}")
        print("Можливо, вхідні дані призводять до неможливих математичних операцій.")
    except OverflowError:
        print("Переповнення при обчисленні. Спробуйте менші значення.")

    input("\nНатисніть Enter для повернення в меню...")


# КРОК 4: Обчислення периметра трикутника
def calculate_triangle_perimeter():
    print("\n--- Обчислення периметра трикутника ---")

    a = get_valid_float_input("Введіть довжину сторони a: ")
    b = get_valid_float_input("Введіть довжину сторони b: ")
    c = get_valid_float_input("Введіть довжину сторони c: ")

    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        print(f"\nПериметр трикутника зі сторонами {a}, {b}, {c} дорівнює {perimeter:.2f}")
    else:
        print("\nЗ введеними сторонами трикутник не існує! (Порушена нерівність трикутника)")

    input("\nНатисніть Enter для повернення в меню...")


# КРОК 5: Використання функцій модуля math
def use_math_functions():
    print("\n--- Використання функцій модуля math ---")

    x = get_valid_float_input("Введіть значення x для обчислень: ")

    try:
        print(f"\nРезультати обчислень для x = {x}:")
        print(f"1. Квадратний корінь: √{x} = {math.sqrt(abs(x)):.4f}")

        if x > 0:
            print(f"2. Натуральний логарифм: ln({x}) = {math.log(x):.4f}")
            print(f"3. Десятковий логарифм: log₁₀({x}) = {math.log10(x):.4f}")
        else:
            print(f"2. Натуральний логарифм: ln({x}) = Неможливо обчислити для x ≤ 0")
            print(f"3. Десятковий логарифм: log₁₀({x}) = Неможливо обчислити для x ≤ 0")

        print(f"4. Синус: sin({x}) = {math.sin(x):.4f}")
        print(f"5. Косинус: cos({x}) = {math.cos(x):.4f}")
        print(f"6. Тангенс: tan({x}) = {math.tan(x):.4f}")

        if x >= 0 and x == int(x) and x <= 20:
            print(f"7. Факторіал: {int(x)}! = {math.factorial(int(x))}")
        else:
            print(f"7. Факторіал: Неможливо обчислити факторіал для {x}")

    except ValueError as e:
        print(f"Помилка обчислення: {e}")
    except OverflowError:
        print("Переповнення при обчисленні.")

    input("\nНатисніть Enter для повернення в меню...")


# КРОК 6: Робота з колом
def calculate_radius_from_circumference(circumference):
    return circumference / (2 * math.pi)


def calculate_area_from_radius(radius):
    return math.pi * radius ** 2


def work_with_circle():
    print("\n--- Робота з колом ---")

    circumference = get_valid_float_input("Введіть довжину кола: ")
    if circumference <= 0:
        print("Довжина кола повинна бути додатним числом!")
        input("\nНатисніть Enter для повернення в меню...")
        return

    radius = calculate_radius_from_circumference(circumference)
    area = calculate_area_from_radius(radius)

    print(f"\nДля кола довжиною {circumference:.2f}:")
    print(f"Радіус = {radius:.4f}")
    print(f"Площа круга = {area:.4f}")

    input("\nНатисніть Enter для повернення в меню...")


# КРОК 7: Форматування чисел
def format_numbers():
    print("\n--- Форматування чисел ---")

    number = get_valid_float_input("Введіть число: ")
    decimals = get_valid_int_input("Введіть кількість знаків після коми: ", 0)

    print(f"\nФорматоване число {number}:")
    print(f"З {decimals} знаками після коми: {number:.{decimals}f}")
    print(f"У форматі з фіксованою точкою: {number:.{decimals}f}")
    print(f"У науковому форматі: {number:.{decimals}e}")
    print(f"У загальному форматі: {number:.{decimals}g}")

    input("\nНатисніть Enter для повернення в меню...")


# КРОК 8: Виведення рівняння
def print_equation(a, b):
    if a == 0:
        if b == 0:
            return "0 = 0 (Рівняння має безліч розв'язків)"
        else:
            return f"{b} = 0 (Рівняння не має розв'язків)"
    else:
        equation = ""

        if a == 1:
            equation += "x"
        elif a == -1:
            equation += "-x"
        else:
            equation += f"{a}x"

        if b > 0:
            equation += f" + {b}"
        elif b < 0:
            equation += f" - {abs(b)}"

        equation += " = 0"

        solution = -b / a
        equation += f" (x = {solution:.4f})"

        return equation


def equation_line():
    print("\n--- Рівняння лінії ---")

    a = get_valid_float_input("Введіть коефіцієнт a: ")
    b = get_valid_float_input("Введіть коефіцієнт b: ")

    equation = print_equation(a, b)
    print(f"\nРівняння лінії: {equation}")

    input("\nНатисніть Enter для повернення в меню...")


# КРОК 9: Персональне вітання
def greet(name, surname):
    return f"Вітаю Вас, {name} {surname}! Раді бачити Вас у нашій програмі."


def personal_greeting():
    print("\n--- Персональне вітання ---")

    name = input("Введіть своє ім'я: ")
    surname = input("Введіть своє прізвище: ")

    greeting = greet(name, surname)
    print(f"\n{greeting}")

    input("\nНатисніть Enter для повернення в меню...")


# Головна функція програми
def main():
    print("МАТЕМАТИЧНО-ГЕОМЕТРИЧНИЙ КАЛЬКУЛЯТОР")

    while True:
        display_menu()
        choice = get_valid_int_input("Виберіть пункт меню (1-8): ", 1, 8)

        if choice == 1:
            manage_coordinates()
        elif choice == 2:
            calculate_expressions()
        elif choice == 3:
            calculate_triangle_perimeter()
        elif choice == 4:
            work_with_circle()
        elif choice == 5:
            equation_line()
        elif choice == 6:
            use_math_functions()
        elif choice == 7:
            personal_greeting()
        elif choice == 8:
            print("\nДякуємо за використання програми. До побачення!")
            break


if __name__ == "__main__":
    main()