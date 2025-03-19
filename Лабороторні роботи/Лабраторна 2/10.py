import math

def calculate_expression(x, y, z):
  return math.exp(x) + 2 * y * z

# Example of use
x = 2
y = 3
z = 4

result = calculate_expression(x, y, z)
print(f"Value of the expression e^{x} + 2*{y}*{z} is equal to {result}")