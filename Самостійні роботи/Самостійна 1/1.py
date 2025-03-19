def validate_text(text):
    return text.replace(" ", "").isalpha()


def validate_number(text):
    return text.isdigit()


def get_answer(question, validation_type=None):
    while True:
        answer = input(question + " ")

        if validation_type == "text":
            if not validate_text(answer):
                print("Помилка! Можна вводити лише букви.")
                continue

        elif validation_type == "number":
            if not validate_number(answer):
                print("Помилка! Можна вводити лише цифри.")
                continue

            # Додаткові перевірки для конкретних числових полів
            if "років" in question and (int(answer) < 1 or int(answer) > 120):
                print("Помилка! Вік повинен бути від 1 до 120 років.")
                continue

            if "номер у списку" in question and (int(answer) < 1 or int(answer) > 33):
                print("Помилка! Номер у списку повинен бути від 1 до 50.")
                continue

            if "групи" in question and (int(answer) < 1 or int(answer) > 60):
                print("Помилка! Номер групи повинен бути від 1 до 999.")
                continue

            if "ЗНО" in question and (int(answer) < 100 or int(answer) > 200):
                print("Помилка! Бал ЗНО повинен бути від 100 до 200.")
                continue

        return answer


def run_questionnaire():
    # Основні питання з валідацією
    questions = {
        "name": ["Ваші прізвище, ім'я, по батькові?", "text"],
        "age": ["Скільки Вам років?", "number"],
        "location": ["Де Ви живете?", "text"],
        "education": ["Де Ви навчаєтесь?", "text"],
        "group": ["Номер Вашої групи?", "number"],
        "number": ["Який Ваш порядковий номер у списку групи?", "number"]
    }

    # Додаткові питання з валідацією
    additional_questions = [
        ["Як справи?", "text"],
        ["Як Ви себе почуваєте?", "text"],
        ["Коли будете вдома?", None],  # Може містити і букви, і цифри
        ["Яку оцінку отримав на ЗНО по українській мові?", "number"],
        ["Сьогодні сонячно?", "text"],
        ["Коли нарешті карантин?", None],  # Може містити і букви, і цифри
        ["Як звати Вашого друга?", "text"],
        ["Ви думаєте вступати у магістратуру?", "text"],
        ["Якого кольору Ваш зошит?", "text"],
        ["Який Ваш настрій сьогодні?", "text"]
    ]

    # Отримання відповідей на основні питання
    answers = {}
    for key, (question, validation) in questions.items():
        answers[key] = get_answer(question, validation)

    # Отримання відповідей на додаткові питання
    additional_answers = []
    for question, validation in additional_questions:
        additional_answers.append(get_answer(question, validation))

    # Виведення результатів
    print("\nРезультати опитування:")
    print(f"Ваше ім'я: {answers['name']}")
    print(f"Ваш вік: {answers['age']}")
    print(f"Ви живете в: {answers['location']}")
    print(f"Ви навчаєтесь в: {answers['education']}")
    print(f"Номер моєї групи - {answers['group']}")
    print(f"Мій порядковий номер у списку групи - {answers['number']}")

    # Виведення додаткових питань та відповідей
    print("\nДодаткові питання та відповіді:")
    for i, (question_data, answer) in enumerate(zip(additional_questions, additional_answers)):
        print(f"{i}. {question_data[0]} {answer}")


if __name__ == "__main__":
    run_questionnaire()