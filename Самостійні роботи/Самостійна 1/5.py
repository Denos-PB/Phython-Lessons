def find_min_max():
    """Основна функція для знаходження мінімального та максимального числа"""
    # Список питань
    questions = [
        "Введіть перше число:",
        "Введіть друге число:",
        "Введіть третє число:"
    ]

    # Отримання відповідей
    numbers = []
    for question in questions:
        while True:
            try:
                number = float(input(question + " "))
                numbers.append(number)
                break
            except ValueError:
                print("Помилка! Потрібно ввести число.")

    # Обчислення результатів
    min_number = min(numbers)
    max_number = max(numbers)

    # Виведення результатів
    print("\nРезультати:")
    print("-" * 30)
    print(f"Введені числа: {', '.join(str(n) for n in numbers)}")
    print(f"Мінімальне число: {min_number}")
    print(f"Максимальне число: {max_number}")


if __name__ == "__main__":
    find_min_max()