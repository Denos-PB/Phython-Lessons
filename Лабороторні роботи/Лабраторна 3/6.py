def input_line_coefficients():
    while True:
        try:
            a = float(input("Введіть коефіцієнт a: "))
            b = float(input("Введіть коефіцієнт b: "))

            if a == 0 and b == 0:
                print("Помилка: Коефіцієнти a і b не можуть бути одночасно нульовими. Спробуйте ще раз.")
                continue

            c = float(input("Введіть коефіцієнт c: "))

            return a, b, c

        except ValueError:
            print("Помилка: Введіть числові значення.")


if __name__ == "__main__":
    print("Введення коефіцієнтів для рівняння прямої ax + by + c = 0")
    a, b, c = input_line_coefficients()
    print(f"Рівняння прямої: {a}x + {b}y + {c} = 0")