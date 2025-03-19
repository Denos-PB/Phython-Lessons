def display_linear_equation(a, b):
    # Handle different cases of coefficients
    if a == 0 and b == 0:
        print("0 = 0 (Identity equation)")
        return

    if a == 0:
        print(f"{b} = 0 (No x term)")
        return

    # Determine x coefficient display
    x_coeff = ''
    if a == 1:
        x_coeff = 'x'
    elif a == -1:
        x_coeff = '-x'
    else:
        x_coeff = f'{a}x'

    # Determine constant term display
    const_term = ''
    if b > 0:
        const_term = f'+ {b}'
    elif b < 0:
        const_term = f'- {abs(b)}'

    # Combine and print the equation
    equation = f"{x_coeff} {const_term} = 0"
    print(f"Equation: {equation}")


# Direct demonstration of function
print("Scenario 1: Standard equation")
display_linear_equation(2, 3)  # 2x + 3 = 0

print("\nScenario 2: Coefficient 1")
display_linear_equation(1, -4)  # x - 4 = 0

print("\nScenario 3: Negative coefficient")
display_linear_equation(-3, 6)  # -3x + 6 = 0

print("\nScenario 4: Zero coefficients")
display_linear_equation(0, 0)  # 0 = 0

print("\nScenario 5: No constant term")
display_linear_equation(5, 0)  # 5x = 0