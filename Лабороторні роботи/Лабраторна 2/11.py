import math
def calculate_expression(x, y):
  numerator = x + math.pi
  denominator = x**2 + y**4 + math.e**3
  return numerator / denominator

# Request for input of x and y values from the user
x = float(input("Enter value x: "))
y = float(input("Enter value y: "))

# Calculation and output of the result
result = calculate_expression(x, y)
print(f"The value of the expression at x = {x} and y = {y}: {result}")