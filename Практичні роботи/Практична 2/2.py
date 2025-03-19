def add_book(book_dict):
    while True:
        book_input = input("Ведіть назву книги та автора, розділеною комою( або stop для завершення):")
        if book_input.lower() == "stop":
            break
        try:
            book, author = book_input.split(',', 1)
            books[book.strip()] = author.strip()
        except ValueError:
            print("Некоректний ввід, спробуйте ще раз")
    return book_dict


def find_book_author(book_dict):
    book_to_find = input("Введіть назву книги для пошуку її автора ")
    if book_to_find in book_dict:
        print(f"Автор книги {book_to_find}: {books[book_to_find]}")
    else:
        print("Книга не знайдена")


def remove_book(book_dict):
    book_to_remove = input("Ведіть назву книги для видалення ")
    if book_to_remove in book_dict:
        del book_dict[book_to_remove]
        print(f"Книга {book_to_remove} успішно видалена.")
    else:
        print("Книга не знайдена в базі данних")
    return book_dict

def list_books(book_dict):
    if book_dict:
        print("Список всіх книг та авторів:")
        for book, author in book_dict.items():
            print(f"{book}: {author}")
    else:
        print("База даних книг порожня.")

def display_menu():
    print("\n===== МЕНЮ УПРАВЛІННЯ КНИГАМИ =====")
    print("1. Додати книгу")
    print("2. Знайти автора за назвою книги")
    print("3. Видалити книгу")
    print("4. Показати всі книги")
    print("5. Вийти з програми")
    print("===================================")


books = {}

menu_options = {
    '1': lambda: add_book(books),
    '2': lambda: find_book_author(books),
    '3': lambda: remove_book(books),
    '4': lambda: list_books(books),
    '5': lambda: "exit"
}

while True:
    display_menu()
    choice = input("Виберіть опцію (1-5): ")

    selected_function = menu_options.get(choice)

    if selected_function:
        result = selected_function()

        if result == "exit":
            print("Дякуємо за використання програми. До побачення!")
            break

        if isinstance(result, dict):
            books = result
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
