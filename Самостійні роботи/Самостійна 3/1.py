def main():
    library = {}

    while True:
        try:
            n = int(input("Введіть кількість книг: "))
            if n <= 0:
                print("Кількість книг повинна бути додатнім числом.")
                continue
            break
        except ValueError:
            print("Помилка! Будь ласка, введіть ціле число.")

    for i in range(n):
        print(f"\nКнига #{i + 1}")
        title = input("Введіть назву книги: ")
        author = input("Введіть автора книги: ")

        while True:
            try:
                pages = int(input("Введіть кількість сторінок: "))
                if pages <= 0:
                    print("Кількість сторінок повинна бути додатнім числом.")
                    continue
                break
            except ValueError:
                print("Помилка! Будь ласка, введіть ціле число для кількості сторінок.")

        library[title] = (author, pages)

    if not library:
        print("Не введено жодної книги.")
        return

    total_pages = sum(book[1] for book in library.values())
    average_pages = total_pages / len(library)

    print(f"\nСередня кількість сторінок у бібліотеці: {average_pages:.2f}")

    print("\nКниги з меншою кількістю сторінок, ніж середнє:")
    found = False
    for title, (author, pages) in library.items():
        if pages < average_pages:
            print(f"- '{title}' автора {author} ({pages} сторінок)")
            found = True

    if not found:
        print("Немає книг з меншою кількістю сторінок, ніж середнє.")


if __name__ == "__main__":
    main()