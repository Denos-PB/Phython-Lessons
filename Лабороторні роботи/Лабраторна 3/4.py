def input_number_in_range(a, b):
    if a > b:
        a, b = b, a
        print(f"Увага: межі діапазону було змінено місцями. Новий діапазон: [{a}, {b}]")

    while True:
        try:
            user_input = input(f"Введіть число в діапазоні [{a}, {b}]: ")

            number = float(user_input)

            if a <= number <= b:
                return number
            else:
                print(f"Помилка: введене число {number} не входить в діапазон [{a}, {b}]")

        except ValueError:
            print("Помилка: введіть коректне число")
        except Exception as e:
            print(f"Непередбачена помилка: {e}")


def test_input_function():
    try:
        print("Тестування функції введення числа в діапазоні [a, b]")
        a = float(input("Введіть нижню межу діапазону (a): "))
        b = float(input("Введіть верхню межу діапазону (b): "))

        number = input_number_in_range(a, b)

        print(f"Успішно введено число {number} в діапазоні [{min(a, b)}, {max(a, b)}]")

    except ValueError as e:
        print(f"Помилка введення: {e}")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")

if __name__ == "__main__":
    test_input_function()