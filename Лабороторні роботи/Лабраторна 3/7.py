def input_coordinates():
    while True:
        try:
            x = float(input("Введіть x-координату точки: "))
            y = float(input("Введіть y-координату точки: "))
            return x, y
        except ValueError:
            print("Помилка: Введіть числові значення для координат.")
        except KeyboardInterrupt:
            print("\nВведення перервано користувачем.")
            exit()
        except Exception as e:
            print(f"Виникла неочікувана помилка: {e}")
            print("Спробуйте ще раз.")

def display_point(x, y):
    try:
        print(f"Точка на площині: ({x}, {y})")
        quadrant = determine_quadrant(x, y)
        print(f"Точка знаходиться в {quadrant} квадраті.")
    except Exception as e:
        print(f"Помилка при відображенні точки: {e}")

def determine_quadrant(x, y):
    if x > 0 and y > 0:
        return "першому"
    elif x < 0 and y > 0:
        return "другому"
    elif x < 0 and y < 0:
        return "третьому"
    elif x > 0 and y < 0:
        return "четвертому"
    elif x == 0 and y != 0:
        return "на осі Y"
    elif x != 0 and y == 0:
        return "на осі X"
    else:
        return "початку координат"

if __name__ == "__main__":
    print("Програма для введення та відображення точки на площині")
    try:
        x, y = input_coordinates()
        display_point(x, y)
    except Exception as e:
        print(f"Критична помилка програми: {e}")
    finally:
        print("Програма завершила роботу.")