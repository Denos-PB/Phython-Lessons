def numbers_in_range(num1, num2, num3, n):
    return [num for num in (num1, num2, num3) if 1 <= num <= n]

# Функція для перевірки, чи є число цілим
def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# Введення даних з перевіркою
while True:
    num1 = input("Введіть перше ціле число: ")
    if is_integer(num1):
        num1 = int(num1)
        break
    else:
        print("Помилка: Перше число має бути цілим. Спробуйте ще раз.")

while True:
    num2 = input("Введіть друге ціле число: ")
    if is_integer(num2):
        num2 = int(num2)
        break
    else:
        print("Помилка: Друге число має бути цілим. Спробуйте ще раз.")

while True:
    num3 = input("Введіть третє ціле число: ")
    if is_integer(num3):
        num3 = int(num3)
        break
    else:
        print("Помилка: Третє число має бути цілим. Спробуйте ще раз.")

while True:
    n = input("Введіть верхню межу інтервалу N (ціле число): ")
    if is_integer(n):
        n = int(n)
        break
    else:
        print("Помилка: N має бути цілим числом. Спробуйте ще раз.")

# Виклик функції та виведення результату
def run_func_result():
    result = numbers_in_range(num1, num2, num3, n)
    if result:
        print(f"Числа, що належать інтервалу [1, {n}]:", result)
    else:
        print(f"Жодне з введених чисел не належить інтервалу [1, {n}].")

if __name__ == '__main__':
    run_func_result()