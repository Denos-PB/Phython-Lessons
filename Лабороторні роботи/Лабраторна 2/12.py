def input_point():
  try:
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))
    return x, y
  except ValueError:
    print("Error: Enter numeric values for the coordinates.")
    return None, None

def output_point(x, y):
  if x is not None and y is not None:
    print(f"Point coordinates: ({x}, {y})")

# Example usage
print("Enter the coordinates of a point:")
x, y = input_point()

if x is not None and y is not None:
  print("\nYou entered the following coordinates:")
  output_point(x, y)
