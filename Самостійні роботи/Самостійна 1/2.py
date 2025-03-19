import math

# Функція для перевірки, чи є число додатним
def is_positive_int(x):
    try:
        x = int(x)
        return x > 0
    except ValueError:
        return False

# Введення даних з перевіркою
while True:
    x = input("Введіть останню цифру вашого списку групи (додатне число): ")
    if is_positive_int(x):
        x = int(x)
        break
    else:
        print("Помилка: Введене число має бути додатним цілим числом. Спробуйте ще раз.")

t = 1

# Обчислення Z
z = (9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t))) * math.exp(x)

# Виведення результату з двома знаками після коми
def print_z():
    print("Z =", round(z, 2))

if __name__ == "__main__":
    print_z()

