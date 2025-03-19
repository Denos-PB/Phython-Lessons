import math

def compare_cotangents(a, b):
    try:
        cot_a = math.cos(a) / math.sin(a) if math.sin(a) != 0 else float('inf') * (1 if math.cos(a) > 0 else -1)
        cot_b = math.cos(b) / math.sin(b) if math.sin(b) != 0 else float('inf') * (1 if math.cos(b) > 0 else -1)

        if abs(cot_a - cot_b) < 1e-10:
            return 0
        elif cot_a > cot_b:
            return 1
        else:
            return -1
    except ZeroDivisionError:
        raise ValueError("Котангенс не визначений для кутів, кратних π")
    except Exception as e:
        raise Exception(f"Помилка при обчисленні котангенсів: {e}")


if __name__ == "__main__":
    try:
        angle1 = float(input("Введіть перший кут (в радіанах): "))
        angle2 = float(input("Введіть другий кут (в радіанах): "))

        result = compare_cotangents(angle1, angle2)

        if result == 1:
            print(f"Котангенс {angle1} більший за котангенс {angle2}")
        elif result == 0:
            print(f"Котангенси кутів {angle1} і {angle2} рівні")
        else:
            print(f"Котангенс {angle1} менший за котангенс {angle2}")
    except ValueError as ve:
        print(f"Помилка: {ve}")
    except Exception as e:
        print(f"Виникла помилка: {e}")