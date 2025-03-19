def create_personal_greeting(last_name, first_name):

    # Capitalize first letters for proper formatting
    last_name = last_name.capitalize()
    first_name = first_name.capitalize()

    greeting = f"Greetings., {first_name} {last_name}! I am glad to welcome you!"
    return greeting


# Prompt user for input and display greeting
last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")

# Generate and print the greeting
personal_greeting = create_personal_greeting(last_name, first_name)
print(personal_greeting)