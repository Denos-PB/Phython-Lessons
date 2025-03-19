def input_quadratic_coefficients():
    print("Введення коефіцієнтів квадратного рівняння ax²+bx+c=0")

    while True:
        try:
            a = float(input("Введіть коефіцієнт a: "))
            if a == 0:
                print("Помилка: коефіцієнт a не може дорівнювати нулю для квадратного рівняння")
            else:
                break
        except ValueError:
            print("Помилка: введіть коректне число для коефіцієнта a")

    try:
        b = float(input("Введіть коефіцієнт b: "))
        c = float(input("Введіть коефіцієнт c: "))
    except ValueError:
        print("Помилка: введіть коректне число")
        return input_quadratic_coefficients()

    print(f"Введені коефіцієнти: a={a}, b={b}, c={c}")
    print(f"Рівняння: {a}x² + ({b})x + {c} = 0")

    return a, b, c


def test_quadratic_equation_input():
    try:
        a, b, c = input_quadratic_coefficients()

        discriminant = b ** 2 - 4 * a * c
        print(f"Дискримінант D = {discriminant}")

        if discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            print(f"Рівняння має два дійсних корені: x1 = {x1}, x2 = {x2}")
        elif discriminant == 0:
            x = -b / (2 * a)
            print(f"Рівняння має один дійсний корінь: x = {x}")
        else:
            real_part = -b / (2 * a)
            imag_part = (abs(discriminant)) ** 0.5 / (2 * a)
            print(f"Рівняння має два комплексних корені:")
            print(f"x1 = {real_part} + {imag_part}i")
            print(f"x2 = {real_part} - {imag_part}i")

    except Exception as e:
        print(f"Помилка при роботі з рівнянням: {e}")


if __name__ == "__main__":
    test_quadratic_equation_input()