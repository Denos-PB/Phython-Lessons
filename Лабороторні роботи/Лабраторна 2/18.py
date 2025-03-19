def calculate_function(a, x):
    # Break down the function step by step
    term1 = x ** 5
    term2 = abs(x)
    term3 = x ** 3
    term4 = abs(a)
    term5 = x ** 2
    term6 = a ** 8

    # Calculate the function value
    result = abs(term1 + term2 - term3) - term4 + term5 + term6

    return result


# Demonstrate the function with various inputs
print("Function Calculation Demonstration:")

# Test cases with different input values
test_cases = [
    (2, 3),  # Positive a and x
    (-1, 4),  # Negative a, positive x
    (0, -2),  # Zero a, negative x
    (1, 0),  # x is zero
    (-3, -5)  # Both a and x are negative
]
# Calculate and print results for each test case
for a, x in test_cases:
    result = calculate_function(a, x)
    print(f"f({a}, {x}) = {result}")