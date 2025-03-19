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

if __name__ == "__main__":
    print("Введення коєфіцієнтфів для квадратичного рівняння")
    a, b, c = input_quadratic_coefficients()