def input_positive_real_number():
    while True:
        try:
            number = float(input("Введіть додатне дійсне число: "))
            if number <= 0:
                print("Помилка: Число повинно бути додатним. Спробуйте ще раз.")
                continue
            return number
        except ValueError:
            print("Помилка: Введено некоректне значення. Введіть дійсне число.")
        except KeyboardInterrupt:
            print("\nВведення перервано користувачем.")
            raise
        except Exception as e:
            print(f"Виникла неочікувана помилка: {e}")
            print("Спробуйте ще раз.")

if __name__ == "__main__":
    try:
        positive_number = input_positive_real_number()
        print(f"Ви ввели додатне число: {positive_number}")
    except KeyboardInterrupt:
        print("Програма завершена користувачем.")
    except Exception as e:
        print(f"Критична помилка програми: {e}")