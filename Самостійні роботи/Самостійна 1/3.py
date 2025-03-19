import math

import math

def f(x):
    """
    Обчислює значення функції:
    f(x) = 0.5 - 4*sqrt(|x|), якщо x >= 0
    f(x) = (sin(x^2))^2 / |x+1|, якщо x < 0
    """
    if x >= 0:
        return 0.5 - 4 * math.sqrt(abs(x))
    else:
        return (math.sin(x**2)**2) / abs(x + 1)

# Протестуємо функцію для різних значень x
test_values = [-2, -1, -0.5, 0, 0.5, 1, 2]

def run_result():
    print("Значення функції для різних x:")
    print("-" * 30)
    print("x\t\tf(x)")
    print("-" * 30)

    for x in test_values:
        try:
            result = f(x)
            print(f"{x:.2f}\t\t{result:.4f}")
        except Exception as e:
            print(f"{x:.2f}\t\tПомилка: {e}")

if __name__ == "__main__":
    run_result()