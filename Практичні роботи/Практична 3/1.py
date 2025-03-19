def input_students():
    students = []
    print("Введіть імена студентів та їх оцінки. Для завершення введіть 'стоп'.")
    while True:
        name = input("Введіть ім'я студента: ").strip().lower()
        if name == "стоп":
            break
        try:
            grade = float(input("Введіть оцінку студента (0-100): "))
            if 0 <= grade <= 100:
                students.append((name, grade))
            else:
                print("Оцінка повинна бути від 0 до 100. Спробуйте ще раз.")
        except ValueError:
            print("Помилка! Введіть числове значення для оцінки.")


    return students

def main():
    students = input_students()

    if not students:
        print("Жодного студента не введено.")
        return

    average = sum(grade for _, grade in students) / len(students)
    print(f"\nСередній бал групи: {average:.2f}")

    print("\nСтуденти з балами нижче середнього:")
    for name, grade in students:
        if grade < average:
            print(f"{name.capitalize()}: {grade:.2f}")

if __name__ == "__main__":
    main()